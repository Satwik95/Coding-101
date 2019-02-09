class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # thanks to lee215 for his solution!
        # https://leetcode.com/problems/maximum-product-subarray/discuss/183483/Easy-and-Concise-Python

        if nums ==[]:
            return 0
        a = nums
        b = nums[::-1]
        for i in range(1,len(nums)):
            a[i] *= a[i-1] or 1
            b[i] *= b[i-1] or 1
        
        return max(a+b)
