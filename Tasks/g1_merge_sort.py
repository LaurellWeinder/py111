from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) == 1:
		return container
	else:
		middle = len(container) // 2
		c1 = sort(container[:middle])
		c2 = sort(container[middle:])
		merge(container, c1, c2)
	return container


def merge(container, c1, c2):
	i = j = k = 0
	while i < len(c1) and j < len(c2):
		if c1[i] < c2[j]:
			container[k] = c1[i]
			i += 1
		else:
			container[k] = c2[j]
			j += 1
		k += 1
	while i < len(c1):
		container[k] = c1[i]
		i += 1
		k += 1
	while j < len(c2):
		container[k] = c2[j]
		j += 1
		k += 1
	return container


