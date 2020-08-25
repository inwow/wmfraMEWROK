
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