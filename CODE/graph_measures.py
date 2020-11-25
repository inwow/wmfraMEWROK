
# Python script for computing simple graph measures
# Input 1: Measure (EdgeCount, AverageDegree, AverageWeightedDegree, EdgeDensity, Diameter, AverageClustering)
# Input 2: Edge_file
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
(1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
=================================================================================================
"""

import networkx as nx
import itertools
import sys

measure = sys.argv[1]
in_file = sys.argv[2]

G = nx.read_edgelist(in_file, comments='#',data=(('metric',float),))
G.remove_edges_from(nx.selfloop_edges(G))

if measure == "EdgeCount":
  	print( str(G.number_of_edges()) )
  
elif measure == "AverageDegree":