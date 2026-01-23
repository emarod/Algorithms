from collections import defaultdict
input = [[0,1], [1,2], [2, 3], [0,3], [0,6], [3,4], [5,6], [6,1]]
num_courses = 7

graph = defaultdict(list)
visited = set()

for i in input:
  src, dst = i
  graph[src].append(dst)

def it_dfs(node):
  stack = []
  stack.append((node, graph[node]))
  # Iterative DFS
  while stack:
    node, neigh = stack.pop()
    visited.add(node)
    print(node, end=",")
    for n in neigh:
      stack.append((n, graph[n]))
  print()

for course in range(num_courses):
  if course not in visited:
    it_dfs(course)