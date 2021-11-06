# Stock Market Network Indicators

The codes in the 'StockMarkNetIndicators' repository can be used to filter cross-correlation matrices of stocks in a financial market to construct network of stocks based on Minimum Spanning Tree (MST) and a chosen threshold. Thereafter, the filtered network in the form of edge list or file can be characterized by computing several network measures including edge-based curvature measures.

## Code Details:

### The following script can be used to filter the cross-correlation matrices and generate edge files and node files of the filtered networks:
* mst_wt.py : Python script to generate a weighted or unweighted filtered minimum spanning tree + thresholded network from the we