# Python Linked List

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node
    
    def print_list(self):
        if self.head == None:
            print("Empty List")
            return
        
        itr = self.head
        optstr = ""
        while itr:
            optstr += (str(itr.data)+"-->")
            itr = itr.next
        print(optstr)

    def insert_at_end(self, data):
        if self.head is None:
            node = Node(data)
            self.head = node
            return
        itr = self.head
        while itr.next != None:
            itr = itr.next
        node = Node(data)
        itr.next = node
    
    def insert_values(self, data):
        for i in data:
            self.insert_at_end(i)
    
    def get_ll_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def remove_at(self, pos):
        if pos < 0 or pos >= self.get_ll_length():
            print("Invalid Pos")
            raise Exception("Invalid Position")
        
        if self.head is None:
            print("Empty List")
            return

        if pos == 0:
            self.head = self.head.next
            return

        itr = self.head
        for i in range(0, pos-1):
            itr = itr.next
        itr.next = itr.next.next

    def insert_at(self, pos, data):
        if pos < 0 or pos >= self.get_ll_length():
            raise Exception("Invalid Pos")
        
        if pos == 0:
            self.insert_at_begining(data)
        
        if pos == self.get_ll_length():
            self.insert_at_end(data)

        itr = self.head
        for i in range(pos-1):
            itr = itr.next
        node = Node(data, itr.next)
        itr.next = node
    
    def insert_after_value(self, insert_after, data):
        itr = self.head
        while itr:
            if itr.data == insert_after:
                node = Node(data, itr.next)
                itr.next = node
                return
            itr = itr.next

        print("Element Not Found")
    
    def remove_by_value(self, value):
        itr = self.head
        count = 0
        while itr:
            if itr.data == value:
                self.remove_at(count)
                return
            itr = itr.next
            count += 1
        print("Value not found")


if __name__ == '__main__':
    ll = LinkedList()
    ll.print_list()
    ll.insert_values([1,2,3,4,5])
    ll.insert_values(["Hello", "There"])
    ll.print_list()
    print(ll.get_ll_length())
    ll.remove_at(0)
    ll.remove_at(2)
    ll.print_list()
    print(ll.get_ll_length())
    ll.insert_at(3, 6)
    ll.insert_at(4, "Well")
    ll.print_list()
    ll.insert_after_value(6, 7)
    ll.insert_after_value("Well", "well")
    ll.print_list()
    ll.remove_by_value(6)
    ll.remove_by_value("well")
    ll.print_list()
    print(ll.get_ll_length())

    # ll.insert_at_begining(1)
    # ll.insert_at_begining(2)
    # ll.insert_at_begining(3)
    # ll.insert_at_end(4)
    # ll.insert_at_end(5)
    
