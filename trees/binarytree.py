class Node:
    """ Node level data structure for binary tree"""

    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.right_child = None
        self.left_child = None


class BinaryTree:
    """ Implementation of binary tree data structure """

    def __init__(self):
        self.root = None

    def add(self, value):
        """
        Add a node with the specific value to the binary tree
        """
        if self.root is None:
            self.root = Node(value, None)
        else:
            self._add(value, self.root)


    def _add(self, value, current_node):
        """
        Traverse the binary tree and add node with specified value in appropriate place
        """
        if value < current_node.value:
            if current_node.left_child:
                self._add(value, current_node.left_child)
            else:
                current_node.left_child = Node(value, current_node)

        else:
            if current_node.right_child:
                self._add(value, current_node.right_child)
            else:
                current_node.right_child = Node(value, current_node)

    def find(self, value):
        """
        Find a node in the binary tree with a specified value
        Returns the value if found
        """
        node = self._find(value, self.root)
        return node.value
        
    def _find(self, value, current_node):
        """
        Find a node with the specified value
        Returns the node if found
        Preorder traversal - root, left, right
        """
        if current_node:
            if current_node.value == value:
                return current_node
            elif value < current_node.value:
                return self._find(value, current_node.left_child)
            else:
                return self._find(value, current_node.right_child)

    def _findmin(self, current_node):
        """
        Find the minimum value node which is a child of the argument node
        """
        if current_node.left_child:
            self._findmin(current_node.left_child)
        else:
            return current_node

    def delete(self, value):
        """ Find a node with a specified value, and delete if it exists """
        node = self._find(value, self.root)
        if node:
            self._delete(node)

    def _delete(self, node):
        """
        Remove a specified node from the tree
        Transplants any children back to the tree before deleting the node
        For no children, no transplant occurs
        For one child, the child is transplanted back to the parent
        For two children, the smallest child of the node to be removed replaces it
        """
        # No children
        if not node.left_child and not node.right_child:
            self._dereference(node)
        else:
            # Two children
            if node.left_child and node.right_child:
                successor = self._findmin(node.right_child)
            # One child
            elif node.left_child:
                successor = node.left_child
            else:
                successor = node.right_child
            node.value = successor.value
            self._dereference(successor)
        
    def _dereference(self, node):
        """ Remove node from tree by dereferencing """
        parent = node.parent
        if parent.left_child == node:
            parent.left_child = None
        else:
            parent.right_child = None

    def print_tree(self):
        """ Print entire tree """
        self._print_tree(self.root)

    def _print_tree(self, node):
        """ Print the entire tree, inorder traversal """
        if node is not None:
            self._print_tree(node.left_child)
            print(str(node.value) + ' ', end = '')
            self._print_tree(node.right_child)

