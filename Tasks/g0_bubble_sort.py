from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	j = 0
	for k in range(len(container) - 1):
		swapped = False
		for i in range(len(container) - 1 - j):
			if container[i] > container[i + 1]:
				container[i + 1], container[i] = container[i], container[i + 1]
				swapped = True
		if not swapped:
			break
		j += 1
	return container
