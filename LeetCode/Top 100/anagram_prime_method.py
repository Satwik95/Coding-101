class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        
        from collections import defaultdict
        def map_prime_to_Chr():
            n = 101
            p = [1]*(n+1)
            for i in range(3,n+1,2):
                if p[i]:
                    for j in range(i*i,n+1,i):
                        p[j] = 0

            res = [2]
            for i in range(3,n+1):
                if i%2!=0 and p[i]==1:
                    res.append(i)
                    
            h = defaultdict(list)
            for i in range(0,26):
                h[(chr(i+ord('a')))].append(res[i])
                
            return h
        
        map = map_prime_to_Chr()
        
        def prod(p, map):
            base = 1
            for ch in p:
                base *= int(map[ch][0])
            return base
        
        base = prod(p, map)
            
        step = len(p)
        res = []
        for i in range(0,len(s)-step+1):
            subset = s[i:i+step]
            if base==prod(subset, map):
                res.append(i)
                
        return res
            