import matplotlib.pyplot as plt
from src.graph_tools import *
import logging

DEFAULT_PATH = '../input/graph.txt'
DEFAULT_ALGORITHM = 'dfs'
DEFAULT_STORAGE = '../output/'


def get_logger() -> logging.Logger:
    """
    Function that return logger withs style settings

    Returns
    -------
    logging.Logger :
        logger with style settings by logging.StreamHandler

    """
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.INFO)
    fh = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    logger.addHandler(fh)
    return logger


def main(start: object, file_path: str = DEFAULT_PATH,
         algorithm: str = DEFAULT_ALGORITHM, storage: str = DEFAULT_STORAGE) -> bool:
    """
    The main function that call other functions

    Parameters
    ----------
    start : object
        any hashable object
    file_path : str
        directory to file to read graph
    algorithm : str, default: 'dfs'
        the name of the algorithm you want to apply to the graph
    storage : str, default: '../output/'
        directory where you want to save the gif file

    Returns
    -------
    bool :
        True if the file was created and no errors occurred,
        False otherwise

    """
    logger = get_logger()
    fig = plt.figure()
    plt.title(f'{algorithm.upper()} for graph from {file_path}')
    camera = Camera(fig)
    graph = graph_builder(file_path)
    if create_gif(graph, camera, func=algorithm, start=start, source=file_path, storage=storage):
        logger.info("Successful completion of the program!")
        return True
    else:
        logger.error('An error has occurred!')
        return False


if __name__ == '__main__':
    main(start='A', algorithm='bfs')
