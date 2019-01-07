class Solution:
    
    def __init__(self):
        self.res = []
    
    def helper(self,s,i,n):
        if i==len(s)-1:
            val = ""
            for ch in s:
                val+=ch
            val = "("+val+")"
            if(self.isBalanced(val):
               self.res.append(val)  
            return
        s[i] = ")"
        self.helper(s,i+1)
        s[i] = "("
        self.helper(s,i+1)
               
        
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        slots = [""]*2*(n-2)
        # -2 cuz the first and the last will always be fixed
        self.helper(slots,0,2*n)

s = Solution()
               
