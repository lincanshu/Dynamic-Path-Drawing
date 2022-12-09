import os

DELIMITER = ':'
NODES_DELIMITER = ','


def read_graph(file_path: str):
    """
    Function that reads a graph from a text file

    Parameters
    ----------
    file_path : str
        directory to file to read graph

    Returns
    -------
    generator :
        yielding node (any hashable object), list of neighbors
    """
    arr = []
    with open(file_path, 'r') as file:
        for line in file.readlines():
            line = line.strip().split()
            arr.append([int(line[0]), int(line[1])])
    return arr