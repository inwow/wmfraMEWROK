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
		(1) ./louvain-generic/convert -i "insert edge file" -o ./temp/$folder/graph.bin -w ./temp/$folder/graph.weights  
		(2) ./louvain-generic/louvain ./temp/$folder/graph.bin -w ./temp/$folder/graph.weights >& ./temp/$folder/graph.tree

### The following MATLAB 2020a program can be used to compute different traditional market indicators:
* analysis_matlab.m : Matlab code to generate index log-returns, mean market correlation, GARCH volatility, minimum risk Markowitz portfolio. The moving epochs and the price time series are the input parameters to code.

## Data description:

* The data was collected from the public domain of Yahoo finance database for two stock markets in two different countries, namely, USA S&P-500 index for 194 stocks and Japanese Nikkei-225 index for 165 stocks spanning a 32-year period from 2 January 1985 (02-01-1985) to 30 December 2016 (30-12-2016). 

* Archived folders 'USA22d22s' and 'JPN22d22s' contain cross-correlation matrices computed using non-overlapping time windows with epoch of 22 days while folders 'USA22d5s' and 'JPN22d5s' contain cross-correlation matrices computed using overlapping time windows with epoch of 22 days and overlap of 5 days. These cross-correlation matrices were used in the construction of the networks. The above-mentioned archived folder can be downloaded from :  
	(1) Folder 'USA22d22s' -  https://www.imsc.res.in/~asamal/data/StockMarkIndicators/USA22d22s.tar.gz  
	(2) Folder 'USA22d5s'  -  https://www.imsc.res.in/~asamal/data/StockMarkIndicators/USA22d5s.tar.gz  
	(3) Folder 'JPN22d22s' -  https://www.imsc.res.in/~asamal/data/StockMarkIndicators/JPN22d22s.tar.gz  
	(4) Folder 'JPN22d5s'  -  https://www.imsc.res.in/~asamal/data/StockMarkIndicators/JPN22d5s.tar.gz  

* The cross-correlation matrices contained in different files in the above-mentioned archived folders are in the form:  
  "stock1	stock2	Correlation	Distance", 
  where distance is computed as Dista