'''
__author__      = "Hongwei Jin"
__Time__        = "Talk topic at Math 554, April 30, 2013"
'''
import copy
import math
import random
import matplotlib as mpt

def MinCut(graph, t):
    while len(graph) > t:
        start = random.choice(graph.keys())
        finish = random.choice(graph[start])

    # # Adding the edges from the absorbed node:
        for edge in graph[finish]:
            if edge != start:  # this stops us from making a self-loop
                graph[start].append(edge)
                
    # # Deleting the references to the absorbed node and changing them to the source node:
        for edge1 in graph[finish]:
            graph[edge1].remove(finish)
            if edge1 != start:  # this stops us from re-adding all the edges in start.
                graph[edge1].append(start)
        del graph[finish]

    # # Calculating and recording the mincut
    mincut = len(graph[graph.keys()[0]])
    cuts.append(mincut)
    return graph

def FastMinCut(graph):

    if len(graph) < 6:
        return MinCut(graph, 2)
    else :
        t = 1 + int(len(graph) / math.sqrt(2))
        graph_1 = MinCut(graph, t)
        graph_2 = MinCut(graph, t)
        if len(graph_1) > len(graph_2):
            return FastMinCut(graph_2)
        else:
            return FastMinCut(graph_1)
        
#         return min(FastMinCut(graph_1), FastMinCut(graph_2))
    
    
filename = "KargerMinCut.txt"
file1 = open(filename)
graph = {}
cuts = []
edge_num = 0
edge_list = []
# print "Loading from", filename
for line in file1:
    node = int(line.split()[0])
    edges = []
    for edge in line.split()[1:]:
        edges.append(int(edge))      
    graph[node] = edges
    edge_num = edge_num + len(edges)
    edge_list.append(len(edges))
file1.close()

# generate adjacency matrix
f = open('matrix.txt', 'w')
for j in range(1, len(graph) + 1):
    for i in range(1, 201):
        if i not in graph[j]:
            f.write('0 ')
        else:
            f.write('1 ')
    f.write('\n')
f.close()

# # print the general info of the graph.
count = 200
while i < count:
    graph1 = copy.deepcopy(graph)
#     g = MinCut(graph1,2)
    g = FastMinCut(graph1)
    i += 1
    
print "Total edges:" , edge_num / 2
print "Total vertices:", len(graph)
print "Maximum degree:", max(edge_list)
print "Minimum degree:", min(edge_list)
print "average degree:", sum(edge_list) / len(edge_list)
print "Runing times:", len(cuts)
# print "Maxcut is", max(cuts)
# print "Mincut is", min(cuts)
