# Stock Market Network Indicators

The codes in the 'StockMarkNetIndicators' repository can be used to filter cross-correlation matrices of stocks in a financial market to construct network of stocks based on Minimum Spanning Tree (MST) and a chosen threshold. Thereafter, the filtered network in the form of edge list or file can be characterized by computing several network measures including edge-based curvature measures.

## Code Details:

### The following script can be used to filter the cross-correlation matrices and generate edge files and node files of the filtered networks:
* mst_wt.py : Python script to generate a weighted or unweighted filtered minimum spanning tree + thresholded network from the weighted network of cross-correlation values.  

### The following scripts can be used to compute the different network measures for the filtered networks:
* comm_eff.py : Python script to calculate the communcation efficiency of the network
* FormanUndirected.cpp : C++ code to calculate the Forman-Ricci curvature of edges in the network
* graph_measures.py : Python script to calculate the following measures on the network, namely, Number of edges, Average degree, Average Weighted Degree, Edge Density, Average Clustering coefficient
* MengerHaantjesUndirected.py : Python script to compute Menger-curvature and Haantjes-curvature for all the edges in an unweighted network
* network_entropy.py : Python script to calculate network entropy using degree and remaining degree distribution
* OR-Undir.py : Python script to compute the Ollivier-Ricci curvature of edges in the network
* Folder 'louvain-generic' within folder 'CODE' contains the code to compute the Louvain modularity of the network; this is a copy of the open source code made available by the original authors of the method
	
	To run:  
		(1) ./louvain-generic/convert -i "insert edge file" -o ./temp/$f