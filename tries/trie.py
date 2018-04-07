"""
Implementation of Trie data structure using letters as nodes to form words
"""


class Node:

    def __init__(self, value):
        """ Creates a trie node with the given value """
        self.value = value
        self.children = {} # dictionary of value:Node
        self.completes_word_flag = False

    def get_value(self):
        """ Get the value of the node """
        return self.value

    def add_child(self, value):
        """ Add a child node with a given value to this node """
        if value not in self.children:
            self.children[value] = Node(value)

    def remove_child(self, value):
        """ Remove a child node of the given value, if it exists """
        if value in self.children:
            del self.children[value]

    def get_children(self):
        """ Return a dictionary of all the children of this node """
        return self.children

    def get_child(self, value):
        """ Return a child node with a specific value, or None if it does not exist """
        try:
            return self.children[value]
        except:
            return None

    def form_word(self):
        """ Change flag to indicate that this node is the final letter in a word """
        self.completes_word_flag = True

    def is_complete_word(self):
        """ Returns True if the node forms a complete word, else return False """
        return self.completes_word_flag

class Trie:

    def __init__(self):
        """ Create a trie data structure made up of letters which can form words """
        self.root = Node(None)
    
    def add_word(self, word):
        """ Add a string to the trie """
        self._add_word(word, self.root)

    def _add_word(self, word, node):
        for letter in word:
            node.add_child(letter)
            node = node.get_child(letter)
        return

    def find_word(self, word):
        """ Return True if word exists in trie, else return False """
        return self._find_word(word, self.root)

    def _find_word(self, word, node):
        
        for letter in word:
            node = node.get_child(letter)
            if node == None:
                return False
        return True