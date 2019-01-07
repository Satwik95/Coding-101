def f(nums,k):
    for x in nums:
        if abs(x-k) in nums:
            return True
    return False

nums = [10, 15, 3, 7]
print(f(nums,17))

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
