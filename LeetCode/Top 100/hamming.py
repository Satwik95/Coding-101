class Solution:
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        
        # xor the nos, and check the set bits of
        # the res
        
        res = x^y
        #count = 0
        #while res:
        #    count += (res&1)
        #    res >>= 1
        return bin(res).count("1")
        #return count