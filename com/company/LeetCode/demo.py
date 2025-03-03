class Node:
    """Represents a node in the binary tree."""
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = Node(data)
    
    def reverse(self):
        self.head = self._reverse(self.head)

    def _reverse(self, node):
        if not node or not node.next:
            return node
        new_head = self._reverse(node.next)
        node.next.next = node
        node.next = None
        return new_head

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

abc = LinkedList()
abc.append('A')
abc.append('B')
abc.append('C')
abc.display()
abc.reverse()
abc.display()