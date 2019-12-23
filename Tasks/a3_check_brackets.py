def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	Valid examples: "", "()", "()()(()())", invalid: "(", ")", ")("
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	br = []
	if len(brackets_row) == 0:
		return True
	if len(brackets_row) % 2 == 0:
		for i in brackets_row:
			if i == '(':
				br.append(i)
			else:
				br.pop()
		if len(br) == 0:
			return True
		else:
			return False
	else:
		return False

