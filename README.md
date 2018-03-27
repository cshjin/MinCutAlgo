# Min-Cut Algorithm

An implementation of Karger's Min-Cut Algorithm and Karger-Stein Algorithm.

The example is from the open course on [Coursera](https://www.coursera.org/) named [Algorithms: Design and Analysis, Part 1](https://www.coursera.org/course/algo) by Prof.  [Tim Roughgarden](https://www.coursera.org/instructor/~214)

It may have some difference compared with the assignment online, please check the algorithm carefully.

### About the algorithm:
The goal of the algorithm is to find a global min-cut in a graph in polynomial time. The graph is undirected and allows parallel edges. The algorithm chooses an edge randomly and contracts it. The procedure is performed recursively until two nodes remain.

### Reference:
* Karger, David R. "__Global min-cuts in RNC, and other ramifications of a simple min-out algorithm.__" Proceedings of the fourth annual ACM-SIAM Symposium on Discrete algorithms. Society for Industrial and Applied Mathematics, 1993.

* Stoer, Mechthild, and Frank Wagner. "__A simple min-cut algorithm.__" Journal of the ACM (JACM) 44.4 (1997): 585-591.

* Karger, David R., and Clifford Stein. "__A new approach to the minimum cut problem.__" Journal of the ACM (JACM) 43.4 (1996): 601-640.

* Karger, David R., and Debmalya Panigrahi. "__A near-linear time algorithm for constructing a cactus representation of minimum cuts.__" Proceedings of the twentieth Annual ACM-SIAM Symposium on Discrete Algorithms. Society for Industrial and Applied Mathematics, 2009.
