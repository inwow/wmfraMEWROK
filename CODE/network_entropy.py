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
(2) A. Samal, H.K. Pharasi, S. J. Ramaia, H. Kannan, E. Saucan, J. Jost & A. Chakraborti, Network geometry and market instability, R. Soc. Op