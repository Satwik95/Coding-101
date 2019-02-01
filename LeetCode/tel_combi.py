class Solution(object):
    
    def __init__(self):
        self.keypad = {0:"",1:"",2:"abc",
                       3:"def",4:"ghi",5:"jkl",
                       6:"mno",7:"pqrs",8:"tuv",
                       9:"wxyz"}
        self.all = []
        self.digits = ""
        
    def _helper(self, inp, out, i, j):
        # base case
        if inp[i]=='\0':
            out[j]='\0'
            k = 0
            res = ""
            while out[k]!='\0':
                res += out[k]
                k += 1
            self.all.append(res)
            return None
        
        # rec case
        key = self.keypad[inp[i]]
        for i in range(len(self.digits)):
            self._helper(inp, out, i+1, j+1)
        
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        self.digits = digits
        inp = digit+"\0"
        out = [""]*len(inp)
        self._helper(inp, out, 0, 0)
        return self.all
