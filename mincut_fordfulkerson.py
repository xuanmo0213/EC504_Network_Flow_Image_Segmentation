# Python 2.7
# Minimum cut using Ford-Fulkerson Algorithm
# The inputs of this algorithm are a graph stored in a matrix, the source node and the sink node.
# The outputs are the total value of max flow and two sets that belong to either set (left, right).
# The algorithm will also print all edges that cut the graph.


V = 6  # Number of vertices in a graph
# Define a graph and a residual graph
# The graph is stored as a matrix
# Values in the matrix are capacities from one node to another
graph = [[0 for col in range(V)] for row in range(V)]
rgraph = [[0 for col in range(V)] for row in range(V)]
# graph from CLRS Page 710
graph = [
         [0, 16,13,0 ,0, 0 ],
         [0, 0, 10,12,0, 0 ],
         [0, 4, 0, 0, 14,0 ],
         [0, 0, 9, 0, 0, 20],
         [0, 0, 0, 7, 0, 4 ],
         [0, 0, 0, 0, 0, 0 ]
                            ]
src = 0  # source node
sink = 5  # sink node


# BFS: return true if there is a path from source 's' to sink 't'
# in the residual graph
def bfs(rgraph, s, t, parent):
    global V
    visited = [False for i in range(V)]  # create a list to store visited nodes
    visited[s] = True  # mark source node as visited
    parent[s] = -1  # mark parent of s as NIL(-1)
    q = list()  # create an empty queue
    q.insert(0, s)  # push source into the queue

    while len(q) != 0:  # while queue is not empty
        current = q.pop()  # pop from q, give its value to current node
        for adjacent in range(V):  # for each node that is adjacent to current
            # if this node is not visited and it's in the residual graph
            if not visited[adjacent] and rgraph[current][adjacent] > 0:
                q.insert(0, adjacent)  # push this node into the queue
                parent[adjacent] = current  # mark its parent as the current node
                visited[adjacent] = True  # mark the node as visited
    return visited[t]  # return whether sink node is visited


# BFS2: return the visited node if there is a path from source 's' to sink 't'
# in the residual graph
def bfs2(rgraph, s, parent):
    global V
    visited = [False for i in range(V)]  # create a list to store visited nodes
    visited[s] = True  # mark source node as visited
    parent[s] = -1  # mark parent of s as NIL(-1)
    q = list()  # create an empty queue
    q.insert(0, s)  # push source into the queue

    while len(q) != 0:  # while queue is not empty
        current = q.pop()  # pop from q, give its value to current node
        for adjacent in range(V):  # for each node that is adjacent to current
            # if this node is not visited and it's in the residual graph
            if not visited[adjacent] and rgraph[current][adjacent] > 0:
                q.insert(0, adjacent)  # push this node into the queue
                parent[adjacent] = current  # mark its parent as the current node
                visited[adjacent] = True  # mark the node as visited
    return visited  # return the nodes that are visited


# Doing min-cut using Ford-Fulkerson Algorithm,
# and print the edges that are from one segment to another in the graph
# store the nodes that belong to one of the two segments in two lists: left, right
def mincut(graph, s, t):
    global V
    rgraph = [[0 for col in range(V)] for row in range(V)]  # initially, f(e)=0 for all edges
    total_flow = 0  # initialize the total flow
    # initialize the residual graph, and let it be the same as the original graph
    for i in range(V):
        for j in range(V):
            rgraph[i][j] = graph[i][j]

    parent = [0 for i in range(V)]
    while bfs(rgraph, s, t, parent):  # while there is an s-t path

        # get bottleneck
        flow = float("inf")  # initialize the flow of a path
        v = t  # let v be the node along a simple s-t path, initialize it to sink
        while v != s:  # update the minimum value along the path
            u = parent[v]
            flow = min(flow, rgraph[u][v])
            v = parent[v]
        bottleneck = flow

        # run augment
        v = t
        while v != s:  # for each edge in the path
            u = parent[v]
            # update the residual graph
            rgraph[v][u] += bottleneck  # if e is a forward edge,  f(e) <- f(e)+b
            rgraph[u][v] -= bottleneck  # if e is a backward edge, f(e) <- f(e)-b
            v = parent[v]

        total_flow += bottleneck  # get the total values of flows

    # get all nodes that are visited in the updated residual graph
    parent = [0 for i in range(V)]
    visited = bfs2(rgraph, s, parent)

    # classify the nodes into two segments in the graph
    left1 = list()
    right1 = list()
    m = 0
    n = 0
    for i in range(V):
        for j in range(V):
            if visited[i] and not visited[j]:
                left1.insert(m,i)
                right1.insert(n,j)
                m = m + 1
                n = n + 1
    left = list(set(left1))
    right = list(set(right1))
    print 'The cutting edges are:'
    for i in range(V):
        for j in range(V):
            if visited[i] and not visited[j] and graph[i][j]:
                print "%d---%d" % (i, j)
    return left, right, total_flow

# test
# CLRS Page 710
left, right, total_flow = mincut(graph, src, sink)
print 'The two segments are:'
print "left = " + str(left)
print "right = " + str(right)
print "The total value of flows is: " + str(total_flow)
