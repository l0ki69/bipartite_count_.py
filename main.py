def read_file():
    k = 0
    with open("True.txt") as file_handler:
        buf = []
        for line in file_handler:
            k += 1
            line = line.replace(" " ,"").replace("\n" ,'')
            for i in range(0 ,len(line)):
                buf.append(int(line[i]))
            adj.append(buf[:])
            buf.clear()
    return k

def bfs(graph,start):
    queue = [start]
    G[start] = 1
    C[start] = True
    while queue:
        temp = queue.pop(0)
        for g in graph[temp]:
            if (C[g]):
                #print("g = ", g," G[g] = ", G[g], " temp = ",temp, " G[temp] = " ,G[temp])
                if (G[g] == G[temp]):
                    return False
                continue
            else:
                C[g] = True
                G[g] = G[temp]*(-1)
                queue.append(g)
    return True

#-----------------------------------main---------------------------


adj = []         #graph
m = read_file()

C = [False] * m      #visit
G = [3]*m    #color

# -1 - Red
# 1 - Black

if bfs(adj,0): print("yes, the count is dicotyledonous")
else: print("no count dicotyledonous")




