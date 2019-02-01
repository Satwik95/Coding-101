class Solution(object):
    
    def rh_append(self, ch, prod):
        return int(ch*prod)
    
    def rh_skip(self, ch, prod):
        return int(prod/ch)
    
    def prod_hash(self, p, map):
        base = 1
        for ch in p:
            base *= int(map[ch][0])
        return base
    
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        if len(s)<len(p):
            return []
        
        map = {'a': [2], 'b': [3], 'c': [5], 'd': [7], 'e': [11], 'f': [13], 'g': [17], 'h': [19], 'i': [23],
               'j': [29], 'k': [31], 'l': [37], 'm': [41], 'n': [43], 'o': [47], 'p': [53], 'q': [59], 'r': [61],
               's': [67], 't': [71], 'u': [73], 'v': [79], 'w': [83], 'x': [89], 'y': [97], 'z': [101]}
        res = []
        hp = self.prod_hash(p, map)
        hs = self.prod_hash(s[:len(p)], map)
        
        if hs==hp:
            res.append(0)
            
        for i in range(len(p), len(s)):
            hs = self.rh_append(map[s[i]][0], self.rh_skip(map[s[i-len(p)]][0], hs))
            print(i, hs, hp)
            if hs == hp:
                res.append(i)
        return res

print(Solution().findAnagrams("cbaebabacd", "abc"))