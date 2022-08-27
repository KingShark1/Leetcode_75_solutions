from collections import deque
from operator import le
from typing import List

def alienDictionary(words: List[str]) -> str:
  letters, order, q = {}, "", deque()
  # Initiating graph
  for pos in range(len(words)):
    for let in range(len(words[pos])):
      letters[words[pos][let]] = {'in': 0, 'out': set()}
  
 
  # adding all the first dependencies
  for word in range(len(words)-1):
    letters[words[word][0]]['out'].add(words[word+1][0]) 
    letters[words[word+1][0]]['in'] += 1
  
  # Adding all the dependencies in current word
  for word in words:
    for let_pos in range(len(word)-1):
      if word[let_pos+1] not in letters[word[let_pos]]['out']:
        letters[word[let_pos]]['out'].add(word[let_pos+1])
        letters[word[let_pos+1]]['in'] += 1
  
  # Removing self loops
  for let in letters:
    if let in letters[let]['out']:
      letters[let]['out'].remove(let)
      letters[let]['in'] -= 1

  # Checking for entry point
  for let in letters:
    if letters[let]['in'] == 0:
      q.append(let)
  
  while q:
    let = q.pop()
    for out_let in letters[let]['out']:
      letters[out_let]['in'] -= 1
      if letters[out_let]['in'] == 0:
        q.append(out_let)
    order += let
  return order if len(order) == len(letters) else ""
words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

print(alienDictionary(words=words))