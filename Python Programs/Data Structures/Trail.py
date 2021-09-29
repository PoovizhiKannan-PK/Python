class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_b(self, data):
        self.head = Node(data, self.head)
    
    def insert_at_e(self, data):
        itr = self.head

        while(itr.next):
            itr = itr.next
        
        itr.next = Node(data)
    
    def print_list(self):
        itr = self.head
        opt = ""
        while(itr):
            opt += str(itr.data)+"-->"
            itr = itr.next
        
        print(opt)
    
    def len_list(self):
        itr = self.head
        count = 0
        while itr:
            count += 1
            itr = itr.next
        return count

    def insert_at(self, data, pos):
        if pos > self.len_list():
            print("invalid pos")
            return
        if pos == 0:
            self.insert_at_b(data)
            return
        if pos == self.len_list():
            self.insert_at_e(data)
            return
        itr = self.head
        for i in range(pos-1):
            itr = itr.next
        
        node = Node(data, itr.next)
        itr.next = node
    
    def delete_at(self, pos):
        if pos > self.len_list():
            print("invalid pos")
            return

        if pos == 0:
            self.head = self.head.next    
            return        
        itr = self.head
        for i in range(pos-2):
            itr = itr.next
        
        itr.next = itr.next.next

if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_b(2)
    ll.insert_at_e(4)
    ll.insert_at(1, 0)
    ll.insert_at(5, 3)
    ll.insert_at(3,2)
    ll.print_list()
    ll.delete_at(0)
    ll.print_list()
    ll.delete_at(4)
    ll.print_list()
    ll.delete_at(2)
    ll.print_list()
