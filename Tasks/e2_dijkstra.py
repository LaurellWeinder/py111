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
	visited = []
	path = {i: float('inf') for i in g.nodes}
	path[starting_node] = 0
	while len(visited) <= len(path):
		if starting_node not in visited:
			neighbors = sorted(g[starting_node].items(), key=lambda x: getitem(x[1], 'weight'))
			for i in neighbors:
				if i[0][0] not in visited:
					weight = g.edges[starting_node, i[0][0]]['weight'] + path[starting_node]
					print(weight)
					if weight < path[starting_node]:
						path[starting_node] = weight
						print(path)
						visited.append(starting_node)
						print(visited)
			starting_node = neighbors.pop(0)
			print(starting_node)
		return path

G = nx.DiGraph()
G.add_nodes_from("ABCDEFG")
G.add_weighted_edges_from([
	("A", "B", 1),
	("B", "C", 3),
	("C", "E", 4),
	("E", "F", 3),
	("B", "E", 8),
	("C", "D", 1),
	("D", "E", 2),
	("B", "D", 2),
	("G", "D", 1),
	("D", "A", 2),])

print(dijkstra_algo(G, 'A'))
