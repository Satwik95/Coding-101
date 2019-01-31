class Solution(object):
    def __init__(self):
        self.inp = []
        self.out = []
        self.all = []

    def cust_print(self, ar):
        i = 0
        comb = []
        while ar[i] != "\0":
            comb.append(ar[i])
            i += 1
        self.all.append(comb)

    def sub_seq(self, i, j):
        # base case
        if self.inp[i] == "\0":
            self.out[j] = "\0"
            self.cust_print(self.out)
            return
        # including
        self.out[j] = self.inp[i]
        self.sub_seq(i + 1, j + 1)
        # excluding
        self.sub_seq(i + 1, j)
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.inp = nums
        self.inp.append("\0")
        self.out = [None]*len(self.inp)
        self.sub_seq(0,0)
        return self.all

print(Solution().subsets([1,2,3]))
