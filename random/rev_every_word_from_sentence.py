def helper(word):
	return word[::-1]

def main(sentence: str) -> str:
	s = sentence.split(" ")
	s = list(map(helper, s))
	return " ".join(s)

input = "Hello there my name is Manas"
print(main(input))