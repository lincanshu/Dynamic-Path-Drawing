import networkx as nx
from queue import Queue


class Stack:
    """
    Implementation of an abstract data type - a stack, by means of a built-in list

    """
    def __init__(self):
        """
        Constructor create instance field `self.nodes`
        """
        self.nodes = []

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
        return self.nodes.pop()

    def empty(self) -> bool:
        """
        Checking the stack for emptiness

        Returns
        -------
        bool :
            False if stack is not empty, True otherwise

        """
        return not bool(self.nodes)


def traverse_graph(graph: nx.Graph, start: object, collection_class: Queue):
    """
    Non-recursive realization of depth-first search or breadth-first search
    algorithm using `~Stack` or `~queue.Queue` respectively

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object
    collection_class : class, default: `~queue.Queue`
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

    collection = collection_class()
    collection.put(start)
    visited = set()
    while not collection.empty():
        current = collection.get()
        if current in visited:
            continue
        visited.add(current)
        yield current

        for neighbor in graph.neighbors(current):
            if neighbor not in visited:
                collection.put(neighbor)


def dfs(graph: nx.Graph, start: object):
    """
    Non-recursive realization of depth-first search algorithm using `~Stack`

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object

    Returns
    -------
    object :
        function `traverse_graph()` call result with argument `~Stack`
    """
    return traverse_graph(graph, start, Stack)


def bfs(graph: nx.Graph, start: object):
    """
    Non-recursive realization of breadth-first search algorithm using `~queue.Queue`

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    start : object
        any hashable object

    Returns
    -------
    object :
        function `traverse_graph()` call result with argument `~queue.Queue`
    """
    return traverse_graph(graph, start, Queue)
