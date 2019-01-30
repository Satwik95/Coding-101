class Solution(object):
    
    def __init__(self):
        self.inp = ""
        self.out = []
        self.count = 0
    
    def subSeq(self, i, j):
        # base case
        if self.inp[i]=="\0":
            self.out[j] = "\0"
            res = ""
            k = 0
            while self.out[k]!='\0':
                res += self.out[k]
                k+=1
            print(res)
            return self.count + 1 if res==res[::-1] else self.count
        # include
        self.out[j] = self.inp[i]
        return self.subSeq(i+1, j+1)
        # dont include
        return self.subSeq(i+1, j)
        
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        self.inp = s+'\0'
        self.out = [None]*len(self.inp)
        return self.subSeq(0,0)

s = Solution()
print(s.countSubstrings("aaa"))
