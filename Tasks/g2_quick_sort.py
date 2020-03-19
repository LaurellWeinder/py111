from typing import Collection, TypeVar
from random import randint

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	low = 0
	high = len(container) - 2
	pivot = (low + high) // 2
	while low != high:
		if len(container) <= 1:
			return container
		else:
			if container[low] < container[pivot]:
				low += 1
				continue
			elif container[high] > container[pivot]:
				high -= 1
				continue
			else:
				container[low], container[high] = container[high], container[low]
	else:
		sort(container[:pivot])
		sort(container[pivot:])
	return container
