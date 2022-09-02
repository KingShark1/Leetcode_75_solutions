class TrieNode:
	def __init__(self) -> None:
		self.children = {}
		self.end_of_word = False

class WordDictionary:
	def __init__(self):
		self.root = TrieNode()
		self.max_word_length = 0

	def addWord(self, word: str) -> None:
		cur = self.root
		for c in word:
			if c not in cur.children:
				cur.children[c] = TrieNode()
			cur = cur.children[c]
		self.max_word_length = max(self.max_word_length, len(word))
		cur.end_of_word = True
		return

	def search(self, word: str) -> bool:
		if len(word) > self.max_word_length:
			return False
		
		def searchHelper(start_index, root):
			for i in range(start_index, len(word)):
				c = word[i]
				if c == '.':
					for children in root.children.values():
						if searchHelper(i + 1, children):
							return True

					return False

				else:
					if c not in root.children:
						return False

					root = root.children[c]

			return root.end_of_word

		return searchHelper(0, self.root)

word_dictionary = WordDictionary()
word_dictionary.addWord("bad")
word_dictionary.addWord("dad")
word_dictionary.addWord("mad")
print(word_dictionary.search("pad"))
print(word_dictionary.search("bad"))
print(word_dictionary.search(".ad"))
print(word_dictionary.search("b.."))