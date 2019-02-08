class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=="":
            return 0
        if len(s)==1:
            return 1
        visited = {}
        max_len = 0
        start = end = 0
        while end<len(s):
            if s[end] in visited:
                # start might have already crossed previous duplicate
                start = max(start, visited[s[end]]+1)
            visited[s[end]] = end
            max_len = max(max_len, end-start+1)
            end +=1 
        return max_len