class Node:
    # in Class we need value and pointer
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def add_to_tail(self, value):
        new_node = Node(value, None)

        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:   
            self.tail.next_node = new_node    
            self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value, None)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:   
            new_node.next_node = self.head 
            self.head = new_node

    def contains(self, value):        
        if not self.head:
            return False

        current = self.head

        while current:
            if current.value == value:    
                return True
            else:
                current = current.next_node 
        return False
    
    def dequeue(self):
      if not self.head:
        return None
      else:
        self.head = self.head.next_node

    def len(self):
        count = 0
        current = self.head

        while current:
            count += 1
            current = current.next_node
        return count


# Setting up a LinkedList for testing
ll = LinkedList()
ll.add_to_tail(1)
ll.add_to_tail(2)
ll.add_to_tail(4)
ll.add_to_tail(5)
ll.add_to_tail(6)

print(ll.len())     # should return 5
print(ll.head.value)    # should return 1
print(ll.head.next_node.next_node.value)    # should return 4
ll.dequeue()    # will remove 1 from head
ll.dequeue()    # will remove 2 from new head
print(ll.head.value)    # As new head, should return 4 
print(ll.len())     # should return 3