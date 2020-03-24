from typing import Hashable, List
import networkx as nx
from Tasks.a1_my_queue import Queue

q = Queue()

def bfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an breadth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node for search
	:return: list of nodes in the visited order
	"""
	visited = [start_node]
	q.enqueue(start_node)
	while len(q) > 0:
		start_node = q.dequeue()
		neighbors = list(g.neighbors(start_node))
		for neigh in neighbors:
			if neigh not in visited:
				visited.append(neigh)
				q.enqueue(neigh)
	return visited
