"""
==================================
Program to compute Menger and Haantjes curvature for edges in unweighted and 
undirected network.
Written by: Areejit Samal
Reference:
(1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
(2) E. Saucan, A. Samal & J. Jost. A simple differential geometry for complex networks. Network Science, 1-28 (2020). doi:10.1017/nws.2020.42.
(3) E. Saucan, A. Samal & J. Jost, A Simple Differential Geometry for Networks and Its Generalizations In: H. Cherifi, S. Gaito, J. Mendes, E. Moro, L. Rocha (Eds) Complex Networks and Their Applications VIII. COMPLEX NETWORKS 2019. Studies in Computational Intelligence, Vol. 881. Springer. 

Input 1: Edge_file 
Input 2: Out_file     
==================================
"""

import networkx as nx
import math
import sys

# Creating the undirected and unweighted graph from edge file
print ("-"*25)
G = nx.Graph()
count=0
for i in open(sys.argv[1], 'r'):
	e = i.strip().split('\t')
	if e[0]!=e[1]:
		G.add_edge(e[0], e[1], weight = 1)
	if e[0]==e[1]:
		count += 1 	

nnodes=G.numbe