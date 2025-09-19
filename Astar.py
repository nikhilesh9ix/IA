def Astar(graph, start, goal, h):
  openlist((start,h[start],0,[start]))
  visited=set()
  while openlist:
open_list.sort()
current,f,g,path=openlist.pop(0)
if current==goal:
  print("goal reached")
  print("path:","->".join(path))
  print("Total cost:",g)
if current in visited:
  continue
visited.add(current)
for neighbour,cost in graph[current]:
  if neighbour not in visited:
    g_new=g+cost
    f_new=g_new+h[neighbour]
    openlist.append(neighbour,f_new,g_new,path+[neighbour])
graph = { 'A':[('B':2),('C':4)],
        B D 3, E7
        C F2
        D g3
        EG2
        FG1
        'G' = []

h={'A'=7,'B'=6,'C'=5,'D'2,e2,f1,g0}

Astar(graph,'A','G',h)
