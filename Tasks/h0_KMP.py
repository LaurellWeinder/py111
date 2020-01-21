from typing import Optional, Sequence


def kmp_algo(inp_string: str, substr: str) -> Optional[int]:
	"""
	Implementation of Knuth-Morrison-Pratt algorithm

	:param inp_string: String where substr is to be found (haystack)
	:param substr: substr to be found in inp_string (needle)
	:return: index where first occurrence of substr in inp_string started or None if not found
	"""
	prefix_list = []
	def prefix_fun(prefix_str: str) -> Sequence[int]:
		"""
		Prefix function for KMP

		:param prefix_str: substring for prefix function
		:return: prefix values table
		"""

		def prefix_sub_func(subsubstr: str) -> int:
			"""
			[False, True, True]
			:param subsubstr:
			:return:
			"""
			prefix_sub_list = [False] * (len(subsubstr) - 1)
			for i in range(1, len(subsubstr)):
				prefix_sub_list[i - 1] = subsubstr[:i] == subsubstr[-i:]

			for i in range(len(prefix_sub_list) -1, -1, -1):
				if prefix_sub_list[i]:
					return i + 1
			return 0

		for i in range(len(prefix_str)):
			prefix_list.append(prefix_sub_func(prefix_str[:i + 1]))
		return prefix_list

	prefix_fun(substr)

	i = j = 0
	while i < len(inp_string):
		if inp_string[i] == substr[j]:
			i += 1
			j += 1
		if j == len(substr):
			return i - j
		else:
			if j == 0:
				i += 1
			else:
				j = prefix_list[j - 1]
	else:
		return None




