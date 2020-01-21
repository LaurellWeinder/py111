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
	visited = set()
	path = {i: float('inf') for i in g.nodes}
	path[starting_node] = 0
	while len(path) >= len(visited):
		if starting_node not in visited:
			neighbors = sorted(g[starting_node].items(), key=lambda x: getitem(x[1], 'weight'))
			if len(neighbors) == 0:
				starting_node = min(path)
			else:
				for i in neighbors:
					if i[0][0] not in visited:
						weight = g.edges[starting_node, i[0][0]]['weight'] + path[starting_node]
						if weight < path[i[0][0]]:
							path[i[0][0]] = weight
							visited.add(starting_node)
				starting_node = neighbors.pop(0)[0][0]
		else:
			return path
	return path
