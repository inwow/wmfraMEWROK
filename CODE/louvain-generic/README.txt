
-----------------------------------------------------------------------------

Multi-criteria community detection
Version 0.3 - not compatible with the previous version (see below).

Based on the article "Fast unfolding of community hierarchies in large networks"
Copyright (C) 2008 V. Blondel, J.-L. Guillaume, R. Lambiotte, E. Lefebvre

And based on the article "A Generalized and Adaptive Method for Community Detection"
Copyright (C) 2014 R. Campigotto, P. Conde Céspedes, J.-L. Guillaume

This file is part of Louvain algorithm.

Louvain algorithm is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Louvain algorithm is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Louvain algorithm.  If not, see <http://www.gnu.org/licenses/>.

-----------------------------------------------------------------------------

Author   : E. Lefebvre, adapted by J.-L. Guillaume and R. Campigotto
Email    : jean-loup.guillaume@lip6.fr
Location : Paris, France
Time	 : July 2014

-----------------------------------------------------------------------------

Disclaimer:
If you find a bug, please send a bug report to jean-loup.guillaume@lip6.fr
including if necessary the input file and the parameters that caused the bug.
You can also send me any comment or suggestion about the program.

Note that the program is expecting a friendly use and therefore does not make
much verifications about the arguments.

-----------------------------------------------------------------------------


This package offers a set of functions to use in order to compute 
communities on graphs weighted or unweighted. A typical sequence of 
actions is:

1. Conversion from a text format (each line contains a couple "src dest")
./convert -i graph.txt -o graph.bin
This program can also be used to convert weighted graphs (each line contain
a triple "src dest w") using -w option:
./convert -i graph.txt -o graph.bin -w graph.weights
Finally, nodes can be renumbered from 0 to nb_nodes-1 using -r option