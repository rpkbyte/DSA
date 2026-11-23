n = 6 # number of nodes 
e = 7 # number of edges

edges = [(0,1), (0,3), (0,4) , (1,2 ), (1,5), (2,4) , (3,4)]
print(n,e,edges)


# adjList 

adjList = []

for i in range(n):
    adjList.append([])

for edge in edges:
    x = edge[0]
    y = edge[1]
    adjList[x].append(y)
    adjList[y].append(x)


for i in range(n):
    print(i,"->",adjList[i])


# adjacency matrix

adjMatrix = []

for i in range(n):
    list1 = [-1]*n 
    adjMatrix.append(list1.copy())

    
for i in range(e):
    a = edges[i][0]
    b = edges[i][1]
    adjMatrix[a][b] = 1
    adjMatrix[b][a] = 1

for i in adjMatrix:
    print(i)
      
