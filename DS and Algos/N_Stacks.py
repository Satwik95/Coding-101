class N_Stacks:
    def __init__(self,N,capacity):
        self.N = N
        self.capacity = capacity
        self.stack_data = [0]*(capacity)
        self.top_of_stack = [-1]*N
        self.prev_nextIndex = [i+1 for i in range(0,capacity)]
        self.prev_nextIndex[-1]=-1
        self.nextAvailable = 0

    def push_item(self,stack_no,val):
        if stack_no<0 or stack_no>=len(self.top_of_stack):
            print("Invalid no of stack!")
            return
        if self.nextAvailable<0:
            print("Stack Overflow")
            return
        temp = self.nextAvailable #get next available
        self.nextAvailable = self.prev_nextIndex[temp] #update next available
        self.stack_data[temp]=val #update the data in the stack
        self.prev_nextIndex[temp] = self.top_of_stack[stack_no] #after setting the data point back to prev top for that stack no
        self.top_of_stack[stack_no] = temp #update top of stack

    def pop_item(self,stack_no):
        if stack_no<0 or stack_no>=len(self.top_of_stack):
            print("Invalid no of stack!")
            return
        if self.top_of_stack[stack_no]<0:
                  print("Stack Empty!")
                  return        
        top_index = self.top_of_stack[stack_no]
        pop_val = self.stack_data[top_index]
        self.top_of_stack[stack_no] = self.prev_nextIndex[top_index]
        self.prev_nextIndex[top_index] = self.nextAvailable
        self.nextAvailable = top_index
        return pop_val

if __name__=="__main__":
    s = N_Stacks(3,6)
    s.push_item(0,5)
    s.push_item(0,6)
    s.push_item(1,7)
    s.push_item(2,1)
    s.push_item(2,2)
    s.push_item(1,2)
    #s.push_item(0,2)#stack overflow
    s.pop_item(0)
    s.pop_item(0)
    s.pop_item(0)#stack empty
    
