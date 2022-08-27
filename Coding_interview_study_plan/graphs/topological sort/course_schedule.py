from collections import deque

def canFinish(numCourses, prerequisite) -> bool:
  nodes, order, q = {}, [], deque()
  
  
  # Initialize nodes
  for node_id in range(numCourses):
    nodes[node_id] = {'in': 0, 'out': set()}
  for node_id, prev in prerequisite:
    nodes[node_id]['in'] += 1
    nodes[prev]['out'].add(node_id)
  for node_id in nodes.keys():
    if nodes[node_id]['in'] == 0:
      q.append(node_id)
      
  while q:
    node = q.pop()
    for out_id in nodes[node]['out']:
      nodes[out_id]['in'] -= 1
      if nodes[out_id]['in'] == 0:
        q.append(out_id)
    order.append(node)

  return True if len(order) == numCourses else False
 
numCourses = 2
prerequisites = [[1,0],[0,1]]
print(canFinish(numCourses=numCourses, prerequisite=prerequisites))