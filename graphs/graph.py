class Graph:

    def __init__(self):
        """ Create graph """
        self._graph = {} # key = node, value = set of neighbours

    def add(self, value):
        """ Add a value to the graph """
        self._graph[value] = set()

    def find(self, value):
        if value in self._graph:
            return True
        else:
            return False

    def _link(self, node_1, node_2):
        """ Link a node to another node """
        self._graph[node_1].add(node_2)
        self._graph[node_2].add(node_1)

    def print_graph(self):
        """ 
        Print the entire graph
        Returns a list of values
        """    
        [print(node, self._graph[node]) for node in self._graph]