class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s=="":
            return ""
        #return sorted([s[j:i] for i in range(len(s)+1) for j in range(i) if s[j:i]==s[j:i][::-1]], key=lambda x: len(x))[-1]
        best = ""
        
        def grow_from_middle(start, end):
            while start>=0 and end<len(s) and s[start]==s[end]:
                start -= 1
                end +=1
            return s[start+1:end]
        
        for i in range(len(s)):
            # for odd cases
            temp = grow_from_middle(i,i)
            if len(temp)>len(best):
                best = temp
            # for even cases
            temp = grow_from_middle(i,i+1)
            if len(temp)>len(best):
                best = temp
        return best