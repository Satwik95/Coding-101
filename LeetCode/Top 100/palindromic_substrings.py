class Solution(object):
    
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        count = 0
        for i in range(len(s)+1):
            for j in range(i):
                if s[j:i] == s[j:i][::-1]:
                    count += 1
        return count"""
        return sum(s[j:i] == s[j:i][::-1] for i in range(len(s)+1) for j in range(i) )
