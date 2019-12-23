from typing import Any, Sequence, Optional
from random import shuffle


def binary_search(elem: Any, arr: Sequence, low=0, high=None) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	if high is None:
		high = len(arr)
	middle = (high - low) // 2 + low
	if high == low:
		return None
	elif arr[middle] == elem:
		return middle
	elif arr[middle] < elem:
		return binary_search(elem, arr, middle + 1, high)
	elif arr[middle] > elem:
		return binary_search(elem, arr, low, middle)





