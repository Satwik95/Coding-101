class Solution(object):
    
    def __init__(self):
        self.res = []
class Solution(object):
    
    def __init__(self):
        self.res = []
    
    """
    def dfs(self, nums, path):
        if not path in self.res:
            if nums == "":
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
        return count == 0"""
                
    def helper(self, cur, no_op_left, no_unclosed):
        if no_op_left == 0:
            self.res.append(cur + ")"*no_unclosed)
        elif no_unclosed == 0:
            self.helper(cur + "(", no_op_left-1, no_unclosed+1)
        else:
            self.helper(cur + "(", no_op_left-1, no_unclosed+1)
            self.helper(cur + ")", no_op_left, no_unclosed-1)
    
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        self.helper("", n, 0)
        return self.res
    
print(Solution().generateParenthesis(6))
