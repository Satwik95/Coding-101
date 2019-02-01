class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        from collections import Counter
        
        if len(s)<len(p):
            return
        
        step = len(p)
        res = []
        for i in range(0,len(s)-step):
            subset = s[i:i+step]
            if Counter(subset)==Counter(p):
                res.append(i)
                
        return res

print(Solution().findAnagrams("cbaebabacd","abc"))
