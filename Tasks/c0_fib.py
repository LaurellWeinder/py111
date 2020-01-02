def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0:
		raise ValueError
	if 0 < n <= 2:
		return 1
	else:
		return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	fib2 = 1
	fib3 = 1
	if n < 0:
		raise ValueError
	if n == 1:
		return 0
	while n > 1:
		fib2, fib3 = fib3, fib2 + fib3
		n -= 1
	return fib2

