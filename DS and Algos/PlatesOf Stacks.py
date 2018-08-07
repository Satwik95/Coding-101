class PlateOfStacks:
    def __init__(self,capacity):
        self.stack = []
        if capacity<1:
            raise NameError("Nhp!")
        else:
            self.capacity = capacity

    def push_item(self,val):
        if not self.stack:
            self.stack.append([val])
        else:
            if len(self.stack[-1])>=self.capacity:
                self.stack.append([val])
            else:
                self.stack[-1].append([val])

    def pop_item(self):
        if self.stack == []:
            raise NameError("Stack Empty")
        #if len of last stack is 1 then delete that stack
        #else if greater then del stack[-1][-1]
        if len(self.stack[-1])==1:
            p = self.stack.pop()
        else:
            p = self.stack[-1].pop()
        return p
    
if __name__=="__main__":
    s = PlateOfStacks(4)
    items = [1,2,3,4,5,6,7,8,9]
    for i in items:
        s.push_item(i)
    print(s.pop_item())#pop 9
    print(s.pop_item())#pop 8
            
