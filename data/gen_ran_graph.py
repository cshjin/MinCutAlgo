## gen_ran_graph

import random
import numpy.random as nprnd
def main():
#    graph_size = random.randint(1,200)
#    t = nprnd.randint(graph_size, size=random.randint(1, graph_size))
#    print graph_size, len(t)
#
#    for i in range(graph_size+1):
#        print i
#    
#    f = open('random_graph.txt','w')
#    for i in range(1,graph_size+1):
#        st = i + t
#        print st
#        f.write(str(i) +'\t')
#        f.write('\n')
#    f.close()
    n = 100
    p = 0.6
    print random.random()
    for i in range(1,n):
        line = str(i) + '\t'
        for j in range(1, n):
            if random.random() >=p and i != j:
                line+= str(j) + '\t'
        print line
    line = str(1)
    if random.random() >= p:
        line
if __name__ == '__main__':
    main()