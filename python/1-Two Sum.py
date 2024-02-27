class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numMap = {}
        for i, num in enumerate(nums):
            tmp = target - num
            if tmp in numMap:
                return [numMap[tmp], i]
            numMap[num] = i
        
        return[]
