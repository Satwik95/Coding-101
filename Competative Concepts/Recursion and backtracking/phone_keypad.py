class subset:
    def __init__(self,inp,out):
        self.inp=inp
        self.out=out
        self.final_out = set()
    def cust_print(self,ar,N):
        i=0
        fresh_str=""
        while ar[i]!="\0":
            fresh_str+=ar[i]
            i+=1
        if len(fresh_str)==N:
            print(fresh_str)
            self.final_out.add(fresh_str)

    def sub_seq(self,i,j,N):
        #base case
        if self.inp[i]=="\0":
            self.out[j]="\0"
            self.cust_print(self.out,N)
            return
        #including
        self.out[j]=self.inp[i]
        self.sub_seq(i+1,j+1,N)
        #excluding
        self.sub_seq(i+1,j,N)

if __name__=="__main__":
    keypad = {0:"",1:"",2:"abc",3:"def",4:"ghi",5:"jkl",6:"mno",7:"pqrs",8:"tuv",9:"wxyz"}
    inp=input()
    N=len(inp)
    inp_str=""
    for i in range(0,len(inp)):
        inp_str+=keypad[int(inp[i])]
        
    inp_str+="\0"
    out = [""]*len(inp_str)
    obj = subset(inp_str,out)
    obj.sub_seq(0,0,N)
    print(len(obj.final_out))
