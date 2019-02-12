class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        implementation based on https://www.geeksforgeeks.org/subset-sum-queries-using-bitset/
        """
        bit = 1
        cur_sum = 0
        for n in nums:
            cur_sum += n
            bit |= bit<<n
        return (not cur_sum%2!=0 ) and (bit>>(cur_sum//2))&1 == 1