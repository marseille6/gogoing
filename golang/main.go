package main

// 很多的任务， 但是执行时间很长， [] 10000 => []100 * 1000
// 小工具，线上在用
// 超时， 报错终止

import (
	"context"
	"fmt"
	"log"
	"math/rand"
	"time"
)

type Tasks struct {
	BatchNum int           // 每批处理多少条数据
	Datas    []interface{} // 数据
	Handler  HandleTask
}

type HandleTask interface {
	HandleSplitTask(ctx context.Context, data []interface{}) *TaskResult
}

type TaskResult struct {
	Err error
	Res []interface{} // 如果需要返回值，就放在这里
}

// 无法保证按照输入的返回顺序， 如果需要顺序返回请使用 ExecuteTasksOrder ,只会返回一个错误
func (tasks *Tasks) ExecuteTasks(ctx context.Context) ([]*TaskResult, error) {
	if tasks.Datas == nil || tasks.Handler == nil || tasks.BatchNum <= 0 {
		return nil, fmt.Errorf("Invalid input, 检查BatchNum, Data, Handler 都有正确赋值. tasks: %v", tasks)
	}
	now := time.Now().UnixMilli()
	log.Printf("开始执行添加任务, 时间戳: %v", now)

	getAllResult := make(chan struct{})
	defer func() {
		close(getAllResult)
	}()
	datasLen := len(tasks.Datas)

	batch := datasLen / (tasks.BatchNum)
	if datasLen%tasks.BatchNum != 0 {
		batch++
	}
	respResult := make(chan *TaskResult, batch)
	defer func() {
		close(respResult)
	}()
	for i := 0; i < batch; i++ {
		startIndex := i * tasks.BatchNum
		endIndex := startIndex + tasks.BatchNum
		if endIndex > datasLen {
			endIndex = datasLen
		}
		go func(startIndex, endIndex int) {
			defer func() {
				if r := recover(); r != nil {
					log.Printf("超时造成, run time panic: %v, ", r)
				}
			}()
			input := tasks.Datas[startIndex:endIndex]
			// log.Printf("开始执行任务, startIndex: %v, endIndex: %v, input: %v", startIndex, endIndex, input)
			respResult <- tasks.Handler.HandleSplitTask(ctx, input)
		}(startIndex, endIndex)
	}
	allResults := make([]*TaskResult, 0, batch)
	var err error
	go func(taskNum int) {

		defer func() {
			if r := recover(); r != nil {
				log.Printf("超时造成, run time panic: %v, ", r)
			}
		}()

		count := 0
		// 只要有一个任务失败，就返回错误
		for result := range respResult {
			if result != nil && result.Err != nil {
				err = result.Err
				getAllResult <- struct{}{}
				break
			}
			allResults = append(allResults, result)
			count++
			if count == taskNum {
				getAllResult <- struct{}{}
				break
			}
		}
	}(batch)

	// 上一次tick的时间
	var lastTickTime int64
	// 设置超时时间
	for {
		select {
		case <-getAllResult:
			log.Printf("结束执行添加任务, 花费时间: %v ms, err: %v", time.Now().UnixMilli()-now, err)
			return allResults, err
		case <-ctx.Done():
			return allResults, fmt.Errorf("Timeout! Some workers are still running.")
		default:
			// 速率控制
			lastTickTime = TimeLimit(lastTickTime, 2)
			continue
		}
	}
}

func TimeLimit(lastTickTime, timeLimit int64) (now int64) {
	now = time.Now().UnixMilli()
	diff := now - lastTickTime
	if diff >= timeLimit {
		return
	}
	time.Sleep(time.Duration(timeLimit-diff) * time.Microsecond)
	now = time.Now().UnixMilli()
	return
}

func ExecuteTasksOrder(ctx context.Context, tasks *Tasks) ([]*TaskResult, error) {
	return nil, nil
}

type HandlSqure struct {
}

func (this *HandlSqure) HandleSplitTask(ctx context.Context, data []interface{}) *TaskResult {
	if data == nil || len(data) == 0 {
		return nil
	}
	taskResult := new(TaskResult)
	results := make([]interface{}, 0, len(data))
	for _, ele := range data {
		// do something
		res := ele.(int) * ele.(int)
		results = append(results, res)
		taskResult.Err = fmt.Errorf("")

	}
	taskResult.Res = results
	return taskResult
}

func main() {
	//  [] 10000 => 乘方
	tasks := new(Tasks)
	tasks.BatchNum = 100
	nums := make([]interface{}, 0, 10000)
	for i := 0; i < 10000000000; i++ {
		num := rand.Int()
		nums = append(nums, num)
	}
	tasks.Datas = nums
	tasks.Handler = new(HandlSqure)
	ctx, _ := context.WithTimeout(context.Background(), 3*time.Second)

	// 并发执行
	tasks.ExecuteTasks(ctx)

	// 顺序执行
	now := time.Now().UnixMilli()
	for _, ele := range nums {
		_ = ele.(int) * ele.(int)
	}
	log.Printf("单携程执行耗时： %v", time.Now().UnixMilli()-now)
}
