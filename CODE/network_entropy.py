# Code calculates network entropy for degree and remaining degree distribution
# Reference for Network Entropy: R.V. Sole and S. Valverde, Information theory of complex networks: on evolution and architectural constraints. Complex networks. Springer Berlin Heidelberg, 2004. 189-207.
# Packages required: igraph, numpy
# python network_entropy.py inputfile_folder_path 1/0 outputfile
# 1 -- weighted
# 0 -- unweighted
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
(1) S. Venkatesan, R.P. Vivek-Ananth, R.P. Sreejith, P. Mangalapandi, A.A. Hassanali & A. Samal, Network approach towards understanding the crazing in glassy amorphous polymers, Journal of Statistical Mechanics: Theory and Experiment 043305 (2018).
(2) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
=================================================================================================
"""

import igraph as ig
import numpy as np
import sys
import glob as gb
import re

#edge files folder path
infile=sys.argv[1]
weight=bool(sys.argv[2]) #input 1 if weighted; 0 if unweighted
outfile=sys.argv[3]

#function input: dictionary of degree/remaining degree distribution
def entropy_dg(P):
	ent=0
	for key in P:
		prob=float(P[key])/num_nodes
		ent+=prob*np.log2(prob)
	return -1*ent
def entropy_rdg(P):
	ent=0
	for key in P:
		ent+=P[key]*np.log2(P[key])
	return -1*ent

#calculate remaining degree distribution from degree distribution
def rem_deg_dist(P):
	rem_deg=[]
	mean_P=0
	for key in P:
		prob=float(P[key])/num_nodes
		mean_P+=float(key)*prob
	print ('\n<E> ',mean_P,'\n')
	for key in P:
    		prob=float(P[key])/num_nodes
    		q=float(key)*prob/float(mean_P)
    		rem_deg.append((key-1,q))
	return dict(rem_deg)

edgefiles=infile

f=open(outfile,'w')

for fil in gb.glob(edgefiles):

	#Read the edge list; Change parameter