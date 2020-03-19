"""
My little Stack
"""
from typing import Any


class Stack:

	def __init__(self):
		self.stack = []

	def pop(self):
		if len(self.stack) == 0:
			return None
		return self.stack.pop()

	def push(self, elem):
		self.stack.append(elem)

	def peek(self, ind=0):
		ind = ~ind
		return self.stack[ind]

	def clear(self):
		self.stack = []

	def __len__(self):
		return(len(self.stack))


# stack = []
#
#
# def push(elem: Any) -> None:
# 	"""
# 	Operation that add element to stack
#
# 	:param elem: element to be pushed
# 	:return: Nothing
# 	"""
# 	global stack
# 	stack.append(elem)
# 	return None
#
#
# def pop() -> Any:
# 	"""
# 	Pop element from the top of the stack
#
# 	:return: popped element
# 	"""
# 	global stack
# 	if len(stack) == 0:
# 		return None
# 	else:
# 		return stack.pop()
#
#
# def peek(ind: int = 0) -> Any:
# 	"""
# 	Allow you to look at the element in the stack without popping it
#
# 	:param ind: index of element (count from the top)
# 	:return: peeked element
# 	"""
# 	global stack
# 	ind = ~ind
# 	return stack[ind]
#
#
# def clear() -> None:
# 	"""
# 	Clear my stack
#
# 	:return: None
# 	"""
# 	global stack
# 	stack = []
# 	return None
#
#
# def leng():
# 	return len(stack)