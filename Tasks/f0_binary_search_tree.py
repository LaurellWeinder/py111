"""
You can do it either with networkx ('cause tree is a graph)
or with dicts (smth like {'key': 0, 'value': 123, 'left': {...}, 'right':{...}})
"""

from typing import Hashable, Any, Optional, Tuple
# import networkx as nx


tree = {}


def insert(key: Hashable, value: Any) -> None:
	"""
	Insert (key, value) pair to binary search tree

	:param key: key from pair (key is used for positioning node in the tree)
	:param value: value associated with key
	:return: None
	"""

	def ins(key, value, tree):
		if len(tree) == 0:
			tree.update({'key': key, 'value': value, 'left': {}, 'right': {}})
		else:
			if key < tree['key']:
				return ins(key, value, tree['left'])
			elif key > tree['key']:
				return ins(key, value, tree['right'])
			else:
				tree['value'] = value
		return tree
	ins(key, value, tree)
	return None


def remove(key: Hashable) -> Optional[Tuple[Hashable, Any]]:
	"""
	Remove key and associated value from the BST if exists

	:param key: key to be removed
	:return: deleted (key, value) pair or None
	"""
	def recursive_remove(key, tree):
		if key > tree['key']:
			recursive_remove(key, tree['right'])
		elif key < tree['key']:
			recursive_remove(key, tree['left'])
		else:
			if tree['left'] == {} and tree['right'] == {}:
				del tree['key']
				return tree['key']['value']
			elif tree['left'] == {}:
				tree['key'] = tree['right']
			elif tree['right'] == {}:
				tree['key'] = tree['left']
			else:
				min = sorted(tree['right'])
				tree['key'] = tree[min]
				recursive_remove(min, tree)


def find(key: Hashable) -> Optional[Any]:
	"""
	Find value by given key in the BST

	:param key: key for search in the BST
	:return: value associated with the corresponding key
	"""

	def nfind(key: Hashable, tree):
		if key == tree['key']:
			return tree['value']
		elif key > tree['key']:
			return nfind(key, tree['right'])
		elif key < tree['key']:
			return nfind(key, tree['left'])
		else:
			raise KeyError
	return nfind(key, tree)


def clear() -> None:
	"""
	Clear the tree

	:return: None
	"""
	tree = {}
	return None
