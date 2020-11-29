
#!/bin/bash

CXX=g++
CXXFLAGS= -ansi -O5 -Wall
DIRSRC= ./src/
EXEC=louvain convert hierarchy matrix
OBJ1= $(DIRSRC)graph_binary.o $(DIRSRC)louvain.o $(DIRSRC)quality.o $(DIRSRC)modularity.o $(DIRSRC)zahn.o $(DIRSRC)owzad.o $(DIRSRC)goldberg.o $(DIRSRC)condora.o $(DIRSRC)devind.o $(DIRSRC)devuni.o $(DIRSRC)dp.o $(DIRSRC)shimalik.o $(DIRSRC)balmod.o
OBJ2= $(DIRSRC)graph.o 

all: $(EXEC)
