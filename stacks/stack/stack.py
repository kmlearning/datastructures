class Stack(object):
    """ Implementation of stack data structure (FIFO) """

    def __init__(self):
        self.items = []

    def is_empty(self):
        """ 
        Check if stack is empty 
        Returns True or False
        """
        return self.items == []

    def push(self, item):
        """ Add item to "top" of the stack """
        self.items.append(item)

    def pop(self):
        """ Remove top item """
        return self.items.pop()

    def peek(self):
        """ Return top item without altering stack """
        return self.items[-1]

    def size(self):
        """ Get stack size """
        return len(self.items)
