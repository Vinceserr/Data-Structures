class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class List:

    def __init__(self):
        self.head = None

    def __add__(self, other):
        new_node = Node(other)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
    def print(self):
        current = self.head
        while(current):
            print(str(current.data), end=' ')
            current = current.next

newList = List()
newList.__add__("Really")
newList.__add__("Are You")
newList.__add__("Serious")
newList.print()


