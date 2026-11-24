# Queue implementation in Python
class Queue:
    
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")

    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek from empty queue")

    def size(self):
        return len(self.items)
    

n = 6 # number of nodes 
e = 7 # number of edges

edges = [(0,1), (0,3), (0,4) , (1,2 ), (1,5), (2,4) , (3,4)]

adjMatrix = [[0] * n for _ in range(n)]
for u, v in edges:
    adjMatrix[u][v] = 1
    adjMatrix[v][u] = 1

queue = Queue()

visited = [False]*n

ans =[]

queue.enqueue(0)
visited[0] = True
ans.append(0)

while not queue.is_empty():
    node = queue.dequeue()
    
    for i in range(n):
        if adjMatrix[node][i] == 1 and not visited[i]:
            queue.enqueue(i)
            visited[i] = True
            ans.append(i)

print("BFS Traversal:", ans)