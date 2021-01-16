
// File: graph_binary.cpp
// -- graph handling source
//-----------------------------------------------------------------------------
// Community detection
// Based on the article "Fast unfolding of community hierarchies in large networks"
// Copyright (C) 2008 V. Blondel, J.-L. Guillaume, R. Lambiotte, E. Lefebvre
//
// And based on the article "A Generalized and Adaptive Method for Community Detection"
// Copyright (C) 2014 R. Campigotto, P. Conde Céspedes, J.-L. Guillaume
//
// This file is part of Louvain algorithm.
// 
// Louvain algorithm is free software: you can redistribute it and/or modify
// it under the terms of the GNU Lesser General Public License as published by
// the Free Software Foundation, either version 3 of the License, or
// (at your option) any later version.
// 
// Louvain algorithm is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
// GNU Lesser General Public License for more details.
// 
// You should have received a copy of the GNU Lesser General Public License
// along with Louvain algorithm.  If not, see <http://www.gnu.org/licenses/>.
//-----------------------------------------------------------------------------
// Author   : E. Lefebvre, adapted by J.-L. Guillaume and R. Campigotto
// Email    : jean-loup.guillaume@lip6.fr
// Location : Paris, France
// Time	    : July 2014
//-----------------------------------------------------------------------------
// see README.txt for more details


#include <fstream>
#include "graph_binary.h"


Graph::Graph() {
  nb_nodes = 0;
  nb_links = 0ULL;

  total_weight = 0.0L;
  sum_nodes_w = 0;
}

Graph::Graph(char *filename, char *filename_w, int type) {
  ifstream finput;
  finput.open(filename,fstream::in | fstream::binary);
  if (finput.is_open() != true) {
    cerr << "The file " << filename << " does not exist" << endl;
    exit(EXIT_FAILURE);
  }

  // Read number of nodes on 4 bytes
  finput.read((char *)&nb_nodes, sizeof(int));
  if (finput.rdstate() != ios::goodbit) {
    cerr << "The file " << filename << " is not a valid graph" << endl;
    exit(EXIT_FAILURE);
  }
  
  // Read cumulative degree sequence: 8 bytes for each node
  // cum_degree[0]=degree(0); cum_degree[1]=degree(0)+degree(1), etc.
  degrees.resize(nb_nodes);
  finput.read((char *)&degrees[0], nb_nodes*sizeof(unsigned long long));

  // Read links: 4 bytes for each link (each link is counted twice)
  nb_links = degrees[nb_nodes-1];
  links.resize(nb_links);
  finput.read((char *)(&links[0]), nb_links*sizeof(int));

  // IF WEIGHTED, read weights: 10 bytes for each link (each link is counted twice)
  weights.resize(0);
  total_weight = 0.0L;
  if (type==WEIGHTED) {
    ifstream finput_w;