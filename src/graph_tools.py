from celluloid import Camera
import graph_reader as gr
from algorithms import *

SEPARATOR = '/'
DEFAULT_COLOR = 'blue'
MARKED_COLOR = 'green'
EXTENSION = '.gif'
FILENAME_TEMPLATE = "{storage}{algorithm}_animation_(...{source}){extension}"
FRAME_INTERVAL = 600
NODE_SIZE = 500


def get_filename(directory: str) -> str:
    """
    Returns the filename by extracting it from an absolute path

    Parameters
    ----------
    directory : str
        the absolute file path

    Returns
    -------
    str :
        the filename

    """
    return directory.rsplit(SEPARATOR)[-1]


def graph_builder(file_path: str) -> nx.Graph:
    """
    Function that construct networkx.Graph using generator

    Parameters
    ----------
    file_path : str
        directory to file to read graph

    Returns
    -------
    `~networkx.Graph` :
        graph constructing from the text file located in file_path

    """
    graph = nx.DiGraph()
    for nod, neighs in gr.read_graph(file_path):
        for neighbour in neighs:
            graph.add_edge(nod, neighbour)
    return graph


def create_gif(graph: nx.Graph, camera: Camera, start: object, storage: str,
               func: str = 'dfs', source: str = '') -> bool:
    """
    Function that create a gif file using Camera from celluloid

    Parameters
    ----------
    graph : `~networkx.Graph`
        any graph
    camera : Camera
        Camera class object required to create the file
    start : object
        any hashable object that is the start node
    storage : str
        directory where you want to save the gif file
    func : str, default: 'dfs'
        the name of the algorithm you want to apply to the graph
    source : str, default: ''
        directory to the file in which the graph was located
        it's required for title and name of the .gif file

    Returns
    -------
    bool :
        True if the file was created and no errors occurred,
        False otherwise

    """
    functions = {'dfs': dfs,
                 'bfs': bfs}

    file_name = FILENAME_TEMPLATE.format(storage=storage, algorithm=func,
                                         source=get_filename(source),
                                         extension=EXTENSION)
    # nodes_color = [graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()]
    # nx.draw_planar(graph, with_labels=True, node_size=NODE_SIZE, node_color=nodes_color)
    # 绘制边的颜色
    edges_color = [graph.edges[edge].get('color', DEFAULT_COLOR) for edge in graph.edges()]
    nx.draw_planar(graph, with_labels=True, node_size=NODE_SIZE, edge_color=edges_color)
    camera.snap()

    for node in functions.get(func)(graph, start):
        graph.nodes[node]['color'] = MARKED_COLOR
        nodes_color = [graph.nodes[node].get('color', DEFAULT_COLOR) for node in graph.nodes()]
        nx.draw_planar(graph, with_labels=True, node_size=NODE_SIZE,
                       node_color=nodes_color)
        camera.snap()
    animation = camera.animate(FRAME_INTERVAL)
    animation.save(file_name, writer='imagemagick')
    return True
