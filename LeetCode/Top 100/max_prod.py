class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # thanks to lee215 for his solution!
        # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/Easy-and-Concise-Python
        import sys
        if nums ==[]:
            return 0
        res = min(nums)
        prod = 1
        for n in nums:
            prod *= n          
            if prod<0:
                prod = 1
                continue
            res = max(res, prod)
        return res