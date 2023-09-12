class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def get_node_at_index(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current
            current = current.next
            count += 1

        return None

# Create a linked list and append some elements
# my_list = LinkedList()
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)

# Display the linked list
# my_list.display()
# print(my_list.get_node_at_index(1).data)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                return
            current = current.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")
    def get_node_at_index(self, index):
        current = self.head
        count = 0

        while current:
            if count == index:
                return current
            current = current.next
            count += 1

        return None

# Example usage:
# dll = DoublyLinkedList()
# dll.append(1)
# dll.append(2)
# dll.append(3)
# dll.prepend(0)
# dll.display() 
# dll.delete(2)
# dll.display()
# print(dll.get_node_at_index(1).prev.data)

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage of the Stack:
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)

# print("Stack contents:", stack.items)
# print("Stack size:", stack.size())
# print("Pop:", stack.pop()) 
# print("Peek:", stack.peek())
# print("Is Empty:", stack.is_empty())