class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for j in range(len(nums)):
            for i in range(len(nums[j+1:])):
                if target-nums[i] == nums[j]:
                    return [j,i]
