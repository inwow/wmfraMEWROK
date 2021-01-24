
# Python script to compute the minimum spanning tree of a network and subsequent addition of edges based on threshold on correlation values.
# Input 1: Edge_file
# Input 2: Whether the network is weighted (1) or unweighted (0)
# Input 2: Out_file
# Input 3: Node_file
"""
=================================================================================================
If you are using this code, kindly cite the following articles:
(1) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Open Sci. 8: 201734 (2021).
=================================================================================================
"""

import networkx as nx
import itertools
import sys
