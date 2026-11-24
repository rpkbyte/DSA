# Stack implementation in Python
class Stack:    
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def size(self):
        return len(self.items)  


n = 6 # number of nodes 
e = 7 # number of edges

edges = [(0,1), (0,3), (0,4) , (1,2 ), (1,5), (2,4) , (3,4)]

adjMatrix = [[0] * n for _ in range(n)]
for u, v in edges:
    adjMatrix[u][v] = 1
    adjMatrix[v][u] = 1


stack = Stack()
visited = [False]*n
ans = []

stack.push(0)
visited[0] = True

while not stack.is_empty():
    node = stack.pop()
    ans.append(node)

    for i in range(n):
        if adjMatrix[node][i] == 1 and not visited[i]:
            stack.push(i)
            visited[i] = True

print("DFS Traversal:", ans)

# adjList 

adjList = []

for i in range(n):
    adjList.append([])

for edge in edges:
    x = edge[0]
    y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)

#dfs by recursion
def dfs(node, visited, ans):
    visited[node] = True
    ans.append(node)

    for neighbor in adjList[node]:
        if not visited[neighbor]:
            dfs(neighbor, visited, ans) 

visited = [False]*n
ans = []
dfs(0, visited, ans)
print("DFS Traversal:", ans)
