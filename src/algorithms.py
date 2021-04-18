import networkx as nx
from queue import Queue


class Stack:
    """
    Implementation of an abstract data type - a stack, by means of a built-in list

    """
    nodes: list = []

    def put(self, node):
        """
        Adding an item to the top of the stack

        Parameters
        ----------
        node : object
            any object

        """
        self.nodes.append(node)

    def get(self) -> object:
        """
        Getting an item from the top of the stack and removing it from their stack
        (essentially an implementation of the pop() method)

        Returns
        -------
        object :
            any object - an item from the top of the stack, or None if the stack is empty

        """
        if not self.empty():
            return self.nodes.pop()
        else:
            return None

    def empty(self) -> bool:
        """
        Checking the stack for emptiness

        Returns
        -------
        bool :
            False if stack is not empty, True otherwise

        """
        if len(self.nodes) > 0:
            return False
        return True


def dfs_bfs_algorithm(graph: nx.Graph, start: object, opt_Queue=Queue):
    """
    Non-recursive realization of depth-first search or breadth-first search
    algorithm using `~Stack` or `~queue.Queue` respectively

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object
    opt_Queue : class, default: `~queue.Queue`
        abstract data type used to implement a specific graph traversal algorithm
        (`~Stack` for depth-first search, `~queue.Queue` for breadth-first search)

    Returns
    -------
    generator :
        yielding node by node of dfs path, on None in error case
    """
    if start not in list(graph.nodes()):
        raise ValueError("The graph does not contain such a node\n"
                         "\t\t\tSet the correct node")

    queue = opt_Queue()
    queue.put(start)
    visited = set()
    while not queue.empty():
        current = queue.get()
        if current in visited:
            continue
        visited.add(current)
        yield current

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                queue.put(neighbor)
