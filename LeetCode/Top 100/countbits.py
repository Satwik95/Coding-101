class Solution:
    
    def countBits(self, num):
        """
        :type num: int
        :rtype: List[int]
        """
        res = []
        for i in range(num+1):
            res.append(bin(i).count("1"))
        return res
        """
        for i in range(1,num+1):
            a = output[i//2] + (i % 2)
            output.append(a)
        """