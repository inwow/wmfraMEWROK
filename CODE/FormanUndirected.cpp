
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
ifstream IN1(argv[2]);
if(!IN1.is_open()) { cout << "Error: node file" << endl; exit(1); }
{
	string line;
	while(getline(IN1,line))
	{
		stringstream DATA(line);
		string name;
		DATA >> name;
			
			bool flag=0;
			for(int i=0;i<NN.size();i++)
			{	
			if(NN[i]==name) { flag=1; break; } 		
			}

			if(flag) { cout << "Error: the node " << name << " appears twice." << endl; exit(1); }
			else
			{
				NN.push_back(name);
				if(nwfl)
				{
					double a=0;
					DATA >> a;
					if(a<=0.0) 	
					{ 
					cout << "Warning: Zero or Negative node weight for node " << name << endl; 
					}
					NW.push_back(a);	
				}
				else
				{
				NW.push_back(1);
				}
			}			
	}
}
IN1.close();

// Print out the number of nodes in the network
int n = NN.size(); 
cout << "The number of nodes in the network is: " << n << endl;

// Create space for Adjacency Matrix and Node Weights
vector<vector<double> > C;
vector<double> FN;
{
	vector<double> temp;
	for(int i=0;i<n;i++) { temp.push_back(0); FN.push_back(0);}
	for(int i=0;i<n;i++) C.push_back(temp);
}

// Check if edges have weights
int ewfl=atoi(argv[3]);
if(ewfl==0) { cout << "The edges in the network have no weights" << endl;}
else        { cout << "The edges in the network have weights" << endl;}

// Read in the edges and their weights
ifstream IN2(argv[4]);
if(!IN2.is_open()) { cout << "Error: edge file" << endl; exit(1); }
{
	int i,j; 
	double a=1;
	string line;
	while(getline(IN2,line))
	{	
		stringstream DATA(line);	
		string sr, tg;
		DATA >> sr;
		DATA >> tg;
		i=-1; j=-1;		
		for(int k=0;k<n;k++)
		{
			if(NN[k]==sr) { i=k; }
			if(NN[k]==tg) { j=k; }
		}			
		if(i==-1) { cout << "Error in edge list - node:" << sr << endl; exit(1); }
		if(j==-1) { cout << "Error in edge list - node:" << tg << endl; exit(1); }	 		

		if(ewfl)
		{		
	 		DATA >> a;