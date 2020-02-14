
// This program computes the Forman curvature for a 
// undirected network, both unweighted and weighted.
// -------------------------------------------------
// Program written by: Areejit Samal (IMSc, Chennai)
// -------------------------------------------------
// -------------------------------------------------
// If you are using this code, kindly cite the following:
// (1) R.P. Sreejith, K. Mohanraj, J. Jost, E. Saucan & A. Samal, Forman curvature for complex networks, Journal of Statistical Mechanics: Theory and Experiment 063206 (2016).
// (2) A. Samal, R.P. Sreejith, J. Gu, S. Liu, E. Saucan & J. Jost, Comparative analysis of two discretizations of Ricci curvature for complex networks, Scientific Reports 8: 8650 (2018). 
// -------------------------------------------------
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>
using namespace std;

int main(int argc, char *argv[])
{

// Check if nodes have weights
int nwfl=atoi(argv[1]);
if(nwfl==0) { cout << "The nodes in the network have no weights" << endl;}
else        { cout << "The nodes in the network have weights" << endl;}

// Read in the node names with weights
vector<string> NN;
vector<double> NW;