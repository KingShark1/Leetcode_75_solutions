def smallest_str_to_remove(s: str) -> int:
	map = {}

	def return_first_recurrence(s: str, map) ->int:
		for ptr in range(len(s)):
			if s[ptr] in map:
				return ptr
			else:
				map[s[ptr]] = 0

	l = return_first_recurrence(s, map)
	r = return_first_recurrence(s[::-1], map)
	
	return len(s) - r - l

print(smallest_str_to_remove("xabbcaqdxry"))