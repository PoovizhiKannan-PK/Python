# Doubly Linked List

class Node:
    def __init__(self, prev = None, data = None, next = None):
        self.prev = prev
        self.data = data
        self.next = next

class DoublyLinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_begining(self, data):
        node = Node(None, data, self.head)

        if self.head is None:
            self.head = node
        else:
            self.head.prev = node
            self.head = node
    
    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(self.head, data, self.head)
            return

        itr = self.head

        while itr.next:
            itr = itr.next

        itr.next = Node(itr, data, None)

    def insert_at(self, pos, data):
        if pos < 0 or pos > self.get_length():
            raise Exception("Invalid position")

        itr = self.head

        if pos == 0:
            self.insert_at_begining(data)
            return
        
        if pos == self.get_length():
            self.insert_at_end(data)
            return

        for i in range(pos-1):
            itr = itr.next

        itr.next = Node(itr, data, itr.next)
    
    def remove_at(self, pos):
        if pos < 0 or pos>= self.get_length():
            raise Exception("Invalid position")

        itr = self.head

        if pos == 0:
            self.head = self.head.next
            self.head.prev = None
            return

        for i in range(pos):
            itr = itr.next
        if itr.next:
            itr.next.prev = itr.prev
        itr.prev.next = itr.next
    
    def print_dll_forward(self):
        itr = self.head
        optstr = ""

        while itr:
            optstr += str(itr.data) + "-->"
            itr = itr.next

        print(optstr)

    def print_dll_backward(self):
        itr = self.get_last_node()
        optstr = ""

        while itr:
            optstr += str(itr.data) + "--<"
            itr = itr.prev

        print(optstr)

    def get_last_node(self):
        itr = self.head

        while itr.next:
            itr = itr.next

        return itr

    def get_length(self):
        itr = self.head
        count = 0

        while itr:
            count += 1
            itr = itr.next

        return count

if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.insert_at_end(0)
    dll.insert_at_begining(1)
    dll.insert_at_begining(2)
    dll.insert_at_begining(3)
    dll.print_dll_forward()
    print(dll.get_length())
    dll.insert_at_end(4)
    dll.insert_at_end(5)
    dll.print_dll_forward()
    print(dll.get_length())
    dll.insert_at(3,"well")
    dll.print_dll_forward()
    dll.insert_at(0,"Well")
    dll.print_dll_forward()
    dll.remove_at(0)
    dll.print_dll_forward()
    dll.remove_at(3)
    dll.print_dll_forward()
    dll.print_dll_backward()