
"""
============================================================================================
A program to compute the Ollivier-Ricci curvature of a given undirected graph.
Reference:
(1) A. Samal, R.P. Sreejith, J. Gu, S. Liu, E. Saucan & J. Jost, Comparative analysis of two discretizations of Ricci curvature for complex networks, Scientific Reports 8: 8650 (2018).
(2) C.C. Ni, Y.Y. Lin, F. Luo & J. Gao. Community detection on networks with ricci flow. Scientific reports 9:9984 (2019).
The following is a modified version of the code that can be found in Chien-Chun Ni's github repository : https://github.com/saibalmars/GraphRicciCurvature.   
============================================================================================
"""

print ("-"*75)
import time, datetime
import cvxpy as cvx
import networkx as nx
import numpy as np
import sys

now = datetime.datetime.now()
start_time = time.time()
print ("Current date and time : ")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print ("="*25)


#If edge has Weight EW = 1 else EW = 0
EW=int(sys.argv[1])

EF=open(sys.argv[3], 'w')

#Creating the graph from the edge file
Graph=nx.Graph()
for i in open(sys.argv[2], 'r'):
	e = i.strip().split('\t')
	if EW == 0 and e[0]!=e[1]:
		Graph.add_edge(e[0], e[1], weight = 1)
	elif EW == 1 and e[0]!=e[1]:
		Graph.add_edge(e[0], e[1], weight = float(e[2]))

edgesize=Graph.number_of_edges()