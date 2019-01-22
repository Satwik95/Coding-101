class Solution(object):
    def binaryGap(self, N):
        """
        :type N: int
        :rtype: int
        """
        
        temp = bin(N)
        loc = []
        for i in range(len(temp)):
            if temp[i]=='1':
                loc.append(i)
        res = 0
        for i in range(len(loc)-1):
            res = max(res, loc[i+1]-loc[i])
            
        return res
