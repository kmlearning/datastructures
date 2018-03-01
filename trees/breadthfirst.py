from binarytree import BinaryTree

class BreadthFirst(BinaryTree):
    """
    Subclass of binary tree implementing breadth first traversal
    Inherits from binary tree superclass
    """

    def __init__(self):
        self.level_traversal = []
        BinaryTree.root = None

    def breadth_first(self):
        """ Return breadth first traversal of binary tree """
        return self._breadth_first(self.root, 0)
    
    def _breadth_first(self, node, level):
        """
        Breadth first traverse of tree
        Returns list of lists where list[depth] is the list of the tree nodes at that level
        """
        if node:
            if level < len(self.level_traversal):
                self.level_traversal[level].append(node.value)
            else:
                self.level_traversal.append([node.value])
            self._breadth_first(node.left_child, level +1)
            self._breadth_first(node.right_child, level +1)
        return self.level_traversal
