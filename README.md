# Big-Data-Assignment-3

Big Data Analytics



Assignment # 3                              Due Date: 19th March 2023

Assignments are to be done in the groups assigned. No late assignments will be accepted.

HONOR POLICY

This assignment is a learning opportunity that will be evaluated based on your ability to think, work through a problem in a logical manner. You may however discuss verbally or via email the assignment with your classmates or the course instructor, and use the Internet to do your research, but the written work should be your own. Plagiarized reports or code will get a zero. If in doubt, ask the course instructor. You should submit your assignment in a zip file following the naming convention. 

Naming Convention: i21xxxx_i21xxxx_i21xxxx.zip

Objectives:

   For this assignment, you are going to implement multiple-source personalized PageRank.

Tasks:

     You must use the dataset which was provided to you in the last Assignment. You have already studied Page-Rank in your class. Now you must implement, multiple-source personalized PageRank algorithm. You will be setting up a Multi-node Hadoop Cluster (three-Node cluster i.e. One Master two Slaves) and executing your code on that cluster. 

Multiple-Source Personalized PageRank:
There is the notion of a source nodes, which is what we're computing the personalization with respect to
When initializing PageRank, instead of a uniform distribution across all nodes, the m source nodes get a mass of 1/m and every other node gets a mass of zero.
Whenever the model makes a random jump (or jumps out of a dangling node), the random jump is always back to one of the source nodes randomly (i.e., 1/m probability to one of the source nodes); this is unlike in ordinary PageRank, where there is an equal probability of jumping to any node.

The following animation illustrates how multi-source personalized PageRank works. In this example, e and a are source nodes.



















If the set of source nodes includes 367, 249, and 145, your program should write the following answer. (i.e., personalized PageRank value, node id)


0.13300 367
0.12234 145
0.12140 249
0.02720 1317
0.01747 264
0.01628 266
0.01615 559
0.01610 5
0.01579 7
0.01507 251





Submission
One of the group members is required to submit a report with supporting screenshots with time stamps. Each member should also explain their findings in the report. Your Zip should have all the files except for the dataset. Please note that you can get called for Demos 

NOTE: Your Report must be PDF and you have to define which group member did which work. 

					




 
