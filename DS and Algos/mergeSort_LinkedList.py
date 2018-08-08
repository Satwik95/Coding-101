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

    def mid(self,head):
        if head==None or head.next==None:
            return head,None
        else:
            slow = head
            fast = slow.next
            while fast!=None and fast.next!=None:
                slow=slow.next
                fast=fast.next.next
        first_last = slow
        first_last.next=None
        return head,slow.next

    def Merge(self,left,right):
        a = LinkedList
        cur = a
        cur_list1=left
        cur_list2=right
        while cur_list1 and cur_list2:
            if cur_list1.data<=cur_list2.data:
                cur.next = cur_list1
                cur_list1=cur_list1.next
            else:
                cur.next = cur_list2
                cur_list2=cur_list2.next
        if cur_list1 == None:
            cur.next = cur_list2
        if cur_list2 == None:
            cur.next = cur_list1
        return a.next

    def mergeSort(self,head):
        if head==None or head.next==None:
            return head
        left,right = self.mid(head)    
        self.mergeSort(left)
        self.mergeSort(right)
        return self.Merge(left,right)
  
if __name__ == '__main__':
    
    ll = LinkedList()
    x = [1,2,3,45,44,8,9]
    for i in x:
        ll.insert_at_end(i)
    ll.print()
    ll.mergeSort(ll.head)
    ll.print()

