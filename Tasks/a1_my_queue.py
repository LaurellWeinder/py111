"""
My little Queue
"""
from typing import Any

queue = []


def enqueue(elem: Any) -> None:
	"""
	Operation that adds element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue.insert(0, elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	return queue.pop()


def peek(ind: int = 0) -> Any:
	"""
	Allow you to look at the element in the queue without dequeueing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	ind = ~ind
	print(ind)
	return queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue = []
	return None
