def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	if n == 0:
		return 1
	else:
		return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""
	fact = 1
	if n < 0:
		raise ValueError
	if n == 0:
		return 1
	while n > 0:
		fact *= n
		n -= 1
	return fact
