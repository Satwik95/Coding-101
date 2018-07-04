class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None

    def insert_at_end(self,data):
        new_node = node(data)
        if self.head==None:
            self.head = new_node
        
        temp = self.head
        while temp.next!=None:
            temp=temp.next

        temp.next = new_node
        new_node.next = None

    def print(self):
        if self.head==None:
            print("Please Insert nodes first!")
            
        temp = self.head
        while temp.next!=None:
            print(temp.data, end = "->")            
            temp=temp.next
        print(temp.data)

    def delete_at_nth(self,n):
        temp = self.head
        i=1
        while i<n-1:
            temp = temp.next
            i+=1

        del_node = temp.next
        temp.next = temp.next.next
        del_node.next = None

    
    def reverse_iterative(self):
        if self.head==None: return

        cur = self.head
        prev = None
        
        while cur.next!=None:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            
        cur.next = prev
        self.head = cur

    def reverse_recursive(self):
            

if __name__ == '__main__':
    
    ll = LinkedList()
    x = [1,2,3,45,44,8,9]
    for i in x:
        ll.insert_at_end(i)
    ll.print()
    ll.delete_at_nth(4)
    ll.print()
    ll.reverse_iterative()
    ll.print()
    


