from typing import Hashable, Mapping, Union
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
	while True:
		if starting_node not in visited:
			neighbors = g[starting_node]
			for i in sorted(neighbors):
				if i not in visited:
					weight = g[starting_node].get('weight') + g[i].get('weight')
					if weight > path[starting_node]:
						path[starting_node] = weight
						visited.append(starting_node)




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

print(G['A'].get())
