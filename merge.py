class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        i = 0
        j = 0
        n1 = len(nums1)
        n2 = len(nums2)
        nums = [0 for i in range(n1 + n2)]
        for index in range(n1 + n2):
            if   i >= n1:
                nums[index] = nums2[j]
                j += 1
            elif j >= n2:
                nums[index] = nums1[i]
                i += 1
            elif nums1[i] >= nums2[j]:
                nums[index] = nums2[j]
                j += 1
            else:
                nums[index] = nums1[i]
                i += 1
        if (n1 + n2) % 2 == 0:
            return (nums[(n1 + n2) // 2 - 1] + nums[(n1 + n2) // 2]) / 2
        return nums[(n1 + n2) // 2]

