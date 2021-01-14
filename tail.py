"""
人一生不会踏进同一条河流
__author__ = 'marseille'
__date__ = '2021/1/12 10:02'
"""
from copy import deepcopy
class tail:
    def recursion(self, arrayIn:list, arrayOutSingle, arrayOutAll):

        if not arrayIn:
            print(arrayOutSingle)
            return arrayOutAll.append(arrayOutSingle)
        for i in range(len(arrayIn)):
            print(i)
            # deepcopy  args[0] = new array()   args[1] = new array()   args[2]:scope(function)  = array
            self.recursion(arrayIn[:i] + arrayIn[i+1:],arrayOutSingle + [arrayIn[i]],arrayOutAll)


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        res = []
        def backtrack(nums, tmp):
            if not nums:
                return res.append(tmp)
            for i in range(len(nums)):
                backtrack(nums[:i] + nums[i+1:], tmp + [nums[i]])
        backtrack(nums, [])
        return res


if __name__ == "__main__":
    a = [1,2,3]
    print(id(a + [4]))
    print(id(a))
    so = tail()

    b = []
    print(so.recursion(a,[],b))
    print(b)