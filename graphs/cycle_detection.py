# # Cycle detection
from collections import defaultdict

graph = defaultdict(list)
input = [[0,1], [1,2], [2, 0], [0,3], [3,4]]

# Graph Construction
for i in input:
  src, dst = i
  graph[src].append(dst)

"""
  States:
 -1 = Not visited
  0 = Visited and in Stack
  1 = Visited, not in Stack
"""
numCourses = 6
states = defaultdict(list)
states = {i : -1 for i in range(numCourses)}

def contains_cycle(node):
  if states[node] == 0:
    return True
  
  if states[node] == 1:
    return False

  states[node] = 0
  for n in graph[node]:
    if contains_cycle(n):
      return True
  
  states[node] = 1
  return False


hasCycle = False
for c in range(numCourses):
  if states[c] == -1:
    if contains_cycle(c):
      hasCycle = True

print(hasCycle)
