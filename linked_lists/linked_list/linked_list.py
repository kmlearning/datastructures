class Node:
    def __init__(self, item):
        """ Create a new node for a linked list """
        self.item = item
        self.next = None

    def get_item(self):
        """ Get the item held at this node """
        return self.item

    def get_next(self):
        """ Get the next node this one points to """
        return self.next

    def set_item(self, item):
        """ Set the item held at this node """
        self.item = item

    def set_next(self, next_ref):
        """ Redirect the pointer to another node """
        self.next = next_ref


class LinkedList:

    def __init__(self):
        """ Create an empty linked list """
        self.head = None

    def add(self, item):
        """ Add a new node to the list """
        if self.head is None:
            self.head = Node(item)
        else:
            new_node = Node(item)
            new_node.set_next(self.head)
            self.head = new_node

    def size(self):
        """ Return the size of the list """
        count = 0
        node = self.head
        while node is not None:
            count += 1
            node = node.get_next()
        return count

    def print_list(self):
        """ Return all items in the linked list """
        node = self.head
        while node is not None:
            print(node.get_item(), end = ' ')
            node = node.get_next()

    def search(self, item):
        """ 
        Check if an item is in the list 
        Return True if it exists, else False
        """
        node = self._search(item)
        if node is not None:
            return True
        else:
            return False

    def _search(self, item):
        """ 
        Return the node which holds a specific item 
        If there is no node with that item, return None
        """
        node = self.head
        while node is not None:
            if node.get_item() == item:
                return node
            node = node.get_next()
        return None

    def remove(self, item):
        """ Find a node with a given value and remove it from the list """
        self._remove(item)

    def _search_parent(self, item):
        """
        Find a node holding a given item
        Return both that node and its parent node as a tuple
        If no node exists holding item, return None
        """
        node = self.head
        prev_node = None
        while node is not None:
            if node.get_item() == item:
                return node, prev_node
            prev_node = node
            node = node.get_next()
        return None

    def _remove(self, item):
        """
        Find a node holding a given item
        Remove it from the list and re-link its neighbours
        """
        node, previous = self._search_parent(item)
        if node is not None:
            if previous is not None:
                previous.set_next(node.get_next())
            else:
                self.head = node.get_next()

