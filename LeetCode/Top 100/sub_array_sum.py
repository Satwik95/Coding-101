class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        #return sum(sum(nums[j:i]) == k for i in range(len(nums)+1) for j in range(i))
        # have to keep track of how many time a particular sub array sum has also occured,
        # hence we can't simply use a dp array, we have to use a hash and keep track of the count
        # of the sum as well
        
        cur_sum, count, dp = 0, 0, {0:1}
        for num in nums:
            cur_sum += num
            count += dp.get(cur_sum-k, 0)
            dp[cur_sum] = dp.get(cur_sum, 0) + 1
        return count

print(subarraySum([1,3,4,8], 7))