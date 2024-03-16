"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/14 11:49'
"""
class HeapSort():
    def __init__(self,A):
        # start_index = 1
        # end_index = len(A) - 1
        self.A = A
        self.heapSize = len(A) - 1

    def left(self,i):
        return 2 * i

    def right(self,i):
        return 2 * i + 1

    def heapify(self,A,i):
        left = self.left(i)
        right = self.right(i)
        if left <= self.heapSize and A[left] > A[i]:
            largest = left
        else:
            largest = i
        if right <= self.heapSize and A[right] > A[largest]:
            largest = right
        if largest != i:
            A[largest], A[i] = A[i], A[largest]
            self.heapify(A,largest)

    def buildHeap(self,A):
        build_start = self.heapSize // 2
        for i in range(build_start,0,-1):
            self.heapify(A,i)

    def heap_sort(self,A):
        for i in range(self.heapSize,1,-1):
            A[1], A[i] = A[i], A[1]
            self.heapSize = self.heapSize - 1
            self.heapify(A,1)
    def main(self):
        self.buildHeap(self.A)
        self.heap_sort(self.A)
        return print(self.A)

a = ['/',5,3,2,-3,-7,45,89,12]
heapSort = HeapSort(a)
heapSort.main()