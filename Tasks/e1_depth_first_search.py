from typing import Hashable, List
import networkx as nx
import Tasks.a0_my_stack as st


def dfs(g: nx.Graph, start_node: Hashable) -> List[Hashable]:
	"""
	Do an depth-first search and returns list of nodes in the visited order

	:param g: input graph
	:param start_node: starting node of search
	:return: list of nodes in the visited order
	"""
	visited = []
	st.push(start_node)
	while st.leng() > 0:
		start_node = st.pop()
		visited.append(start_node)
		neighbors = list(g.neighbors(start_node))
		for neigh in neighbors:
			if neigh not in visited:
				st.push(neigh)
	return visited
