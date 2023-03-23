#!/usr/bin/python3

import sys

graph={}

#   Iterating through each line in the standard input and constructing the graph.

for line in sys.stdin:
    line=line.strip()
    if line.startswith("#"):    #   Condition to check if the line is a comment.
        continue
    from_node, to_node=line.split("\t")
    if from_node not in graph:  #   Condition to check if the source node is already in the dictionary.
        graph[from_node]=[to_node]  #   Adding the source node to the dictionary.
    else:
        graph[from_node].append(to_node)    #   Adding the neighbouring node to the source node.

#   Iterating through the graph dictionary and printing the key-value pairs.

for key, value in graph.items():
    value=str(value).replace("'", "")   #   Replacing the single quotes with empty strings.
    print(key, value)