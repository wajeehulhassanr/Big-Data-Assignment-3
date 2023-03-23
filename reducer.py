#!/usr/bin/python3

import sys

'''

The `pagerank(graph, sources, alpha=0.85, maximum_iterations=100, tolerance=1e-6)`
function initialises a list of PageRank scores for each node in the graph structure,
and a list of personalisation weights for each source node. It then iterates through
the graph structure, calculating the new PageRank score for each node based on its
incoming links and the previous PageRank scores of its neighbours. The personalisation
weights and dangling nodes (nodes with no outgoing links) are also taken into account.
The function stops iterating when the convergence criterion is met or the maximum
number of iterations is reached.

Parameters

----------

    graph : dictionary

        A dictionary that represents the graph structure. Each key is a node in
        the graph structure, and its value is a list of nodes that it links to.

    sources : list

        A list of node ids that are treated as “sources” and given a higher weight
        in the PageRank calculation.

    alpha : float

        A damping factor that determines how much weight is given to incoming links.
        The default value is 0.85.

    maximum_iterations : integer

        The maximum number of iterations to run the algorithm. The default value is 100.

    tolerance : float

        The convergence criterion for the algorithm. If the difference between the current
        and previous PageRank scores is less than tolerance, the algorithm stops iterating.
        The default value is 1e-6.

Returns

-------

    pagerank : list

        A list of tuples, where each tuple contains the PageRank score and the corresponding
        node. The first three tuples in the list correspond to the source nodes, and the
        remaining tuples correspond to the other nodes in the graph structure.


'''

#   Function to implement the Personalised PageRank algorithm for a given graph structure and a set of source nodes.

def pagerank(graph, sources, alpha=0.85, maximum_iterations=100, tolerance=1e-6):
    n=max(int(node) for node in graph.keys())+1 #   Number of nodes in the graph.
    m=len(sources)  #   Number of source nodes.
    pagerank=[0]*n  #   Initialising the PageRank vector.
    personalisation=[0]*n   #   Initialising the personalisation vector.
    weight=1/m  #   Weight of each source node.
    source_nodes=set(sources)   #   Converting the list of source nodes to a set for faster lookup.

    #   Iterating through the graph and assigning the initial PageRank values to the source nodes.

    for source in sources:
        personalisation[source]=weight  #   Assigning the weight of each source node to the personalisation vector.
        pagerank[source]=weight #   Assigning the weight of each source node to the PageRank vector.

    #   Iterating through the graph and assigning the initial PageRank values to the dangling nodes.
    
    for _ in range(maximum_iterations):
        previous_pagerank=pagerank.copy()   #   Copying the previous PageRank vector.
        dangling=[node for node in graph if not graph[node]]    #   Finding the dangling nodes.
        previous_dangling_sum=sum(previous_pagerank[node] for node in dangling) #   Calculating the sum of the PageRank values of the dangling nodes.

        #   Iterating through the graph and calculating the PageRank values of the remaining nodes.

        for node in graph:
            if graph[node]: #   Checking if the node has at least one neighbour.
                pagerank[node]=(1-alpha)/n  #   Adding the teleportation factor to the PageRank value.
                pagerank[node]+=alpha*previous_dangling_sum/n   #   Adding the dangling node factor to the PageRank value.

                #   Iterating through the neighbours of the current node and adding the PageRank values of the neighbours to the current node.

                for neighbour in graph[node]:
                    try:
                        pagerank[node]+=alpha*previous_pagerank[neighbour]/len(graph[neighbour])    #   Adding the PageRank value of the neighbour to the current node.
                    except: #   Handling the case where the neighbour has no neighbours.
                        continue
            else:
                pagerank[node]=(1-alpha)/n+alpha*previous_dangling_sum/n    #   Adding the teleportation and dangling node factors to the PageRank value.
            if node in source_nodes:    #   Checking if the current node is a source node.
                pagerank[node]+=(1-alpha)*personalisation[node] #   Adding the personalisation factor to the PageRank value.
                pagerank[node]+=alpha*previous_dangling_sum*personalisation[node]   #   Adding the dangling node factor to the PageRank value.
            elif node in dangling:  #   Checking if the current node is a dangling node.
                pagerank[node]+=(1-alpha)*weight/m  #   Adding the personalisation factor to the PageRank value.
                pagerank[node]+=alpha*previous_dangling_sum*weight/m    #   Adding the dangling node factor to the PageRank value.
            else:
                pagerank[node]+=(1-alpha)*weight/(n-m)  #   Adding the personalisation factor to the PageRank value.
                pagerank[node]+=alpha*previous_dangling_sum*weight/(n-m)    #   Adding the dangling node factor to the PageRank value.
            pagerank[node]+=alpha*personalisation[node]*(1-sum(graph[node].count(neighbour) for neighbour in sources)/(len(graph[node]) or 1))/m    #   Adding the personalisation factor to the PageRank value.
        norm=sum(abs(pagerank[i]-previous_pagerank[i]) for i in range(n))   #   Calculating the norm of the difference between the current and previous PageRank vectors.
        if norm<tolerance:  #   Checking if the norm is less than the tolerance.
            break
    return pagerank

#   Driver function.

if __name__=="__main__":
    graph={}

    #   Iterating through each line in the standard input and constructing the graph.

    for line in sys.stdin:
        line=line.strip()
        key, value=line.split(" ", 1)
        graph[int(key)]=[int(x) for x in value.strip("[]").split(",")]  #   Adding the source node to the graph dictionary.
    sources=[367, 249, 145]
    pagerank=pagerank(graph, sources)
    sorted_nodes=sorted(((score, node) for node, score in enumerate(pagerank)), reverse=True)   #   Sorting the nodes in descending order of their PageRank values.
    for score, node in sorted_nodes:
        print(f"{score:.5f} {node}")