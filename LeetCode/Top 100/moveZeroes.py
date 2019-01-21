class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count = 0
        for x in nums:
            if x != 0:
                nums[count] = x
                count += 1

        while count < len(nums):
            nums[count] = 0
            count += 1