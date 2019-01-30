class Solution(object):
    
    def __init__(self):
        self.res = []
    
    def dfs(self, nums, path):
        if nums == "":
            if not path in self.res:
                if self.isValid(path):
                    self.res.append(path)
        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path + nums[i])
            
    def isValid(self, s):
        count = 0
        for ch in s:
            if ch == "(": 
                count += 1
            elif ch == ")":
                count -= 1
            if count<0: return False
        return count == 0
                
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        op = "("*n
        cl = ")"*n
        s = op+cl
        self.dfs(s, "")
        return self.res
        
print(Solution().generateParenthesis(5))
