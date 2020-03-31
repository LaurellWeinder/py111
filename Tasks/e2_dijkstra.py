from typing import Hashable, Mapping, Union
from operator import getitem
import networkx as nx


def dijkstra_algo(g: nx.DiGraph, starting_node: Hashable) -> Mapping[Hashable, Union[int, float]]:
    """
    Count shortest paths from starting node to all nodes of graph g
    :param g: Graph from NetworkX
    :param starting_node: starting node from g
    :return: dict like {'node1': 0, 'node2': 10, '3': 33, ...} with path costs, where nodes are nodes from g
    """
    unvisited = {node: float('inf') for node in g.nodes}
    path = {node: float('inf') for node in g.nodes}
    unvisited[starting_node] = 0
    path[starting_node] = 0
    while True:
        neighbors = list(g.neighbors(starting_node))
        for neighbor in neighbors:
            if neighbor not in unvisited:
                continue
            weight = g.edges[starting_node, neighbor]['weight'] + unvisited[starting_node]
            if weight < unvisited[neighbor]:
                unvisited[neighbor] = weight
                path[neighbor] = weight
        del unvisited[starting_node]
        if not unvisited:
            break
        starting_node = sorted(unvisited, key=unvisited.get)[0]
    return path

if __name__ == '__main__':
    pass