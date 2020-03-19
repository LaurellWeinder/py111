"""
My little Queue
"""
from typing import Any


class Queue:

	def __init__(self):
		self.queue = []

	def enqueue(self, elem):
		self.queue.insert(0, elem)

	def dequeue(self):
		if len(self.queue) == 0:
			return None
		else:
			return self.queue.pop()


	def peek(self, ind: int=0):
		if len(self.queue) == 0:
			return None
		else:
			ind = ~ind
			return self.queue[ind]

	def clear(self):
		self.queue = []

	def __len__(self):
		return len(self.queue)
# queue = []
#
#
# def enqueue(elem: Any) -> None:
# 	"""
# 	Operation that adds element to the end of the queue
#
# 	:param elem: element to be added
# 	:return: Nothing
# 	"""
# 	global queue
# 	queue.insert(0, elem)
# 	return None
#
#
# def dequeue() -> Any:
# 	"""
# 	Return element from the beginning of the queue
#
# 	:return: dequeued element
# 	"""
# 	if len(queue) == 0:
# 		return None
# 	else:
# 		return queue.pop()
#
#
# def peek(ind: int = 0) -> Any:
# 	"""
# 	Allow you to look at the element in the queue without dequeueing it
#
# 	:param ind: index of element (count from the beginning)
# 	:return: peeked element
# 	"""
# 	global queue
# 	ind = ~ind
# 	return queue[ind]
#
#
# def clear() -> None:
# 	"""
# 	Clear my queue
#
# 	:return: None
# 	"""
# 	global queue
# 	queue = []
# 	return None
#
#
# def leng():
# 	global queue
# 	return len(queue)