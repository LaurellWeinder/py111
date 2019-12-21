"""
Taylor series
"""
from typing import Union
import math

def ex(x: Union[int, float]) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	e = [1]
	n = 1
	for i in range(100):
		e.append(x ** n / math.factorial(n))
		n += 1
	return sum(e)


def sinx(x: Union[int, float]) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	sin = [x]
	n = 1
	for i in range(10):
		sin.append(((-1) ** n) * (x ** (2 * n + 1) / math.factorial(2 * n + 1)))
		n += 1
	return sum(sin)
