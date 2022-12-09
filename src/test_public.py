import pytest
import os
from main import main, plt
from graph_tools import *
import platform


graph_1 = 'test_source/test_graph_1.txt'
STORAGE = 'test_source/'
NON_EXIST_NODE = 'A'
EXIST_NODE = '1'
DFS = 'dfs'
BFS = 'bfs'

# necessary define operation system
if platform.system() == 'Windows':
    graph_1 = '../' + graph_1
    STORAGE = '../' + STORAGE
elif platform.system() == 'Linux':
    graph_1 = graph_1
    STORAGE = STORAGE


real_graph_1 = {'1': ['12', '13'],
                '12': ['121', '122', '123'],
                '13': ['131', '132'],
                '131': ['1311'],
                '1311': ['13111']}


def test_read_graph():
    assert os.path.exists(graph_1)
    graph = gr.read_graph(graph_1)
    for node, neighbors in graph:
        assert real_graph_1[node].sort() == neighbors.sort()


def test_graph_builder():
    graph = graph_builder(graph_1)
    for node, neighbors in graph.adj.items():
        if node in real_graph_1:
            assert real_graph_1[node].sort() == list(neighbors).sort()


def test_bfs():
    graph = graph_builder(graph_1)
    bfs_path = list(bfs(graph, EXIST_NODE))
    for i in range(len(bfs_path) - 1):
        assert len(bfs_path[i]) <= len(bfs_path[i + 1])


def test_dfs():
    graph = graph_builder(graph_1)
    dfs_path = list(dfs(graph, EXIST_NODE))
    real_nodes_1 = set()
    for node, neighbours in real_graph_1.items():
        real_nodes_1.add(node)
        real_nodes_1.update(set(neighbours))

    for node in list(real_nodes_1):
        assert node in dfs_path


def test_dfs_with_wrong_arg():
    # here we pass a non-existent vertex "A" as an argument
    graph = graph_builder(graph_1)
    with pytest.raises(ValueError):
        _ = list(dfs(graph, NON_EXIST_NODE))


def test_create_gif_creating_gif_file():
    algorithm = BFS
    fig = plt.figure()
    camera = Camera(fig)
    graph = graph_builder(graph_1)
    assert create_gif(graph, camera, func=algorithm, start=EXIST_NODE, source=graph_1, storage=STORAGE)
    file_name = FILENAME_TEMPLATE.format(storage=STORAGE, algorithm=algorithm,
                                         source=get_filename(graph_1),
                                         extension=EXTENSION)
    assert os.path.exists(file_name)


def test_create_gif_with_wrong_arg():
    # here we pass a non-existent vertex "A" as an argument
    algorithm = BFS
    fig = plt.figure()
    camera = Camera(fig)
    graph = graph_builder(graph_1)
    with pytest.raises(ValueError):
        create_gif(graph, camera, func=algorithm, start=NON_EXIST_NODE, source=graph_1, storage=STORAGE)


def test_main_func_create_gif_file():
    algorithm = DFS
    assert main(start=EXIST_NODE, file_path=graph_1, algorithm=algorithm, storage=STORAGE)
    file_name = FILENAME_TEMPLATE.format(storage=STORAGE, algorithm=algorithm,
                                         source=get_filename(graph_1),
                                         extension=EXTENSION)
    assert os.path.exists(file_name)


def test_main_with_wrong_arg():
    # here we pass a non-existent vertex "A" as an argument
    algorithm = DFS
    with pytest.raises(ValueError):
        main(start=NON_EXIST_NODE, file_path=graph_1, algorithm=algorithm, storage=STORAGE)
