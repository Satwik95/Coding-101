"""
Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.
"""


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        h = {}
        for key in nums:
            h[key] = 0

        #print(len(h))
        for i in range(len(nums)):
            if target-nums[i] in h:
                if h[(target-nums[i])] == 1:
                    return [nums.index(target-nums[i]), i]
                else:
                    h[nums[i]] = 1
                
        return x

        
