from collections import defaultdict

class Graph:
	def __init__(self):
		self.graph = defaultdict(list)

	def add(self,u,v):
		self.graph[u].append(v)
		self.graph[v].append(u)

	def print_(self):
		for u in self.graph:
			print(u , "->" , self.graph[u])

	def bfs(self , i , visited):
		l = [i]
		visited[i] = True
		print(i , end=' ')
		while(l):
			for v in self.graph[i]:
				if visited[v]==False:
					print(v , end=" ")
					l.append(v)
					visited[v] = True
			if l:
				l.pop(0)
			if l:
				i = l[0]
			# visited[i] = False




n = 4
g = Graph()

# g.add(1,2)
# g.add(1,3)
# g.add(1,4)
# g.add(2,5)
# g.add(2,6)
# g.add(5,9)
# g.add(5,10)
# g.add(4,7)
# g.add(4,8)
# g.add(7,11)
# g.add(7,12)

g.add(1,2)
g.add(1,3)
g.add(3,1)
g.add(2,3)
g.add(3,4)
g.add(4,4)
print()
g.print_()

visited = [False]*(n+1)

for i in range(1,n+1):
	if visited[i]==False:
		g.bfs(i,visited)