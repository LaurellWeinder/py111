from typing import Any, Sequence, Optional


def binary_search(elem: Any, arr: Sequence) -> Optional[int]:
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	low = 0
	high = len(arr)
	while low < high:
		middle = (high - low) // 2 + low
		if arr[middle] == elem:
			return middle
		elif arr[middle] > elem:
			high = middle - 1
		elif arr[middle] < elem:
			low = middle + 1
	return None



