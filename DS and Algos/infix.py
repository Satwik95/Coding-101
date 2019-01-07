class Infix:
    def __init__(self):
        self.num = []
        self.operator = []
        self.paran = []
        self.ops = "+-*/^"
        self.opParan = "([{"

    def isOperator(self,val):
        if val in self.ops:
            return True
        
    def prec(self,val):
        return self.ops.index(val)

    def openingParan(self,val):
        if val in self.opParan:
            return True
        
    def isPair(self,op,clo):
        if op=="(" and clo==")":
            return True
        elif op=="[" and clo=="]":
            return True
        elif op=="{" and clo=="}":
            return True
        return False

    def calculate(self,exp):
        for i in range(len(exp)):
            print(self.num, self.paran, self.operator)
            if self.isOperator(exp[i]):
                if self.paran == []:
                    if self.operator==[] or self.prec(self.operator[-1])<=self.prec(exp[i]):
                        self.operator.append(exp[i])
                    else:
                        res = self.evaluate()
                        self.num.append(res)
                        self.operator.append(exp[i])
                else:
                    self.operator.append(exp[i])
            elif exp[i].isdigit():
                self.num.append(exp[i])
            else:
                if self.openingParan(exp[i]):
                    self.paran.append(exp[i])
                    self.operator.append(exp[i])
                else:
                    if self.isPair(self.paran[-1],exp[i]):
                        new_exp = ""
                        while self.operator[-1]!=self.paran[-1]:
                            new_exp += str(self.num.pop())
                            new_exp += self.operator.pop()
                            #new_exp.append(self.num.pop())
                            #new_exp.append(self.operator.pop())
                        #remove last bracket which is included
                        #new_exp.append(self.num.pop())
                        new_exp+=str(self.num.pop())
                        #since concatinated from stack gotta reverse it again
                        new_exp = new_exp[::-1]
                        new_exp2=""
                        for x in new_exp:
                            new_exp2+=str(x)
                        print(new_exp2)
                        new_obj = Infix()
                        ans = new_obj.calculate(new_exp2)
                        self.num.append(ans)
                        self.paran.pop()
                        self.operator.pop()
                        
        while self.operator!=[]:
            res = self.evaluate()
            self.num.append(res)
        return self.num.pop()

    def evaluate(self):
        if self.operator==[]:
            return
        op2 = int(self.num.pop())
        op1 = int(self.num.pop())
        sign = self.operator.pop()
        #if self.prec(sign)<self.prec(self.operator[-1]):
            
        if sign=="+":
            return op1+op2
        elif sign=="-":
            return op1-op2
        elif sign=="*":
            return op1*op2
        elif sign=="/":
            return op1/op2
        elif sign=="^":
            return op1**op2
            

if __name__=="__main__":
    s1 = "1+(2+3)*3"
    s2 = "2+[(3-6)/5]"
    s3 = "1*{2+3-[1*(2-1)]+3}"
    s4 = "2^3^4"
    s5 = "(2*5)+4"
    exp = "[3+6]*[3+[2+6]]"
    obj = Infix()
    ans = obj.calculate(exp)
    print(ans)
                
            
        
