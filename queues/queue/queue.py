
class Queue(object):
    """ Implementation of queue data structure (FIFO) """

    def __init__(self):
        """ Create a new, empty queue """
        self.items = []

    def enqueue(self, item):
        """ Add item to end of queue """
        self.items.insert(0, item)

    def dequeue(self):
        """ Remove item from front of queue """
        return self.items.pop()

    def is_empty(self):
        """ 
        Check if queue is empty
        Returns True or False
        """
        return self.items == []

    def size(self):
        """ Returns number of items in the queue """
        return len(self.items)






