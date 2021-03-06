class Subset:
    def __init__(self, inp, out):
        self.inp = inp
        self.out = out
        self.f = 0
        self.count = 0
        self.all = []

    def cust_print(self, ar):
        i = 0
        self.count += 1
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
        print("including",self.out)
        self.sub_seq(i + 1, j + 1)
        # excluding
        print("excluding",self.out)
        self.sub_seq(i + 1, j)


if __name__ == "__main__":
    nums = [1, 5, 8, 12, 12, 35, 35, 35, 61]
    inp = [str(x) for x in nums]
    inp = "abc"
    inp += "\0"
    out = [""] * len(inp)
    obj = Subset(inp, out)
    obj.sub_seq(0, 0)
    print(obj.all)
