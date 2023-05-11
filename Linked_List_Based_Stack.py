class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        new_node = Node(data)                                       # create a new node with the given data
        new_node.next = self.top                                    # set the new node as the new top and update the size
        self.top = new_node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        popped_node = self.top                                     # remove the current top and set the next node as the new top
        self.top = self.top.next
        self.size -= 1
        return popped_node.data

    def peek(self):
        if self.is_empty():
            return None
        return self.top.data                                       # return the data of the current top without removing it

    def is_empty(self):
        return self.top is None                                    # return True if the stack is empty, False otherwise

    def is_full(self):                                             # linked-based stacks are usually not limited by a fixed size, so always return False
        return False

    def get_size(self):                                            # return the current size of the stack
        return self.size
