class Deque(object):
    """ 
    Aka double-ended-queue
    Ordered collection of items
    Similar to queue but with two ends: front and rear
    """

    def __init__(self):
        """ Create empty deque """
        self.items = []

    def add_front(self, item):
        """ Add item to front of deque """
        self.items.insert(0, item)

    def add_rear(self, item):
        """ Add item to rear of deque """
        self.items.append(item)

    def remove_front(self):
        """ Remove and return item at front of deque """
        return self.items.pop(0)

    def remove_rear(self):
        """ Remove and return item at rear of deque """
        return self.items.pop()

    def is_empty(self):
        """
        Check if deque is empty
        Returns True or False
        """
        return self.items == []

    def size(self):
        """ Return number of items in deque """
        return len(self.items)