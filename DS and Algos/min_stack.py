class stack:
    def __init__(self,st1,st2):
        self.st1 = st1
        self.st2 = st2
    def push_item(self,val):
        self.st1.append(val)
        if not self.st2:
            self.st2.append(val)
        else:
            if self.st1[-1]<=self.st2[-1]:
                self.st2.append(val)
    def pop_item(self):
        if self.st1.pop()<=self.st2[-1]:
            self.st2.pop()
    def get_min(self):
        return self.st2[-1]

if __name__=="__main__":
    st1 = []
    st2 = []
    s = stack(st1,st2)
    items = [7,9,6,5,5,1]
    for val in items:
        s.push_item(val)

    s.pop_item()#pop 1
    print(s.get_min())#min should be 5
