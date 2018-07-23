class subset:
    def __init__(self,inp,out):
        self.inp=inp
        self.out=out

    def cust_print(self,ar):
        i=0
        while ar[i]!="\0":
            print(ar[i],end="")
            i+=1
        print("",end=",")
            
    def sub_seq(self,i,j):
        #base case
        if self.inp[i]=="\0":
            self.out[j]="\0"
            print(i,j,end="-")
            self.cust_print(self.out)
            return
        #including
        self.out[j]=self.inp[i]
        self.sub_seq(i+1,j+1)
        #excluding
        self.sub_seq(i+1,j)

if __name__=="__main__":
    inp="abcabc"
    inp+="\0"
    out = [""]*len(inp)
    obj = subset(inp,out)
    obj.sub_seq(0,0)
