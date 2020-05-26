# K-Nearest Neighbors Algorithm

This assignment aims to familiarize you with the mechanism of two widely-used classification methods: k-nearest neighbors (KNN).

For k-nearest neighbors, please use Euclidean distance to compute the distance between any pair of nodes.

## Model specifications
For KNN, set k = 3.

**The following design choice in implementation purely aims to ease auto- grading on HackerRank.** 

We ensure each attribute is named by a **non-negative integer**, and each class label is named by a **positive integer**. Since we are to use HackerRank for grading, we have to eliminate additional randomness and generate the deterministic results. We therefore enforce the following rule in this assignment: In the event of ties, always choose the attribute or label with the smallest value. Namely,
When determining the nearest neighbors, if at most one of two training instances can be included into the set of k nearest neighbors, but they have two distinct labels L1 and L2, include the one with smaller of L1 and L2.
- In prediction, if both label L1 and L2 have the same number of training instances at a leaf node of a DT, predict the smaller of L1 and L2.
- In prediction, if both label L1 and L2 have the same number of training instances in the set of k nearest neighbors, predict the smaller of L1 and L2.

## Input Format and Sample
Each input dataset contains training instances followed by test instances in a format adapted from the libsvm format. Each line has the form

    [label] [attribute 1]:[value 1] [attribute 2]:[value 2] . . .
which is space-separated. As mentioned above, the name of each attribute, e.g., [attribute 2], is a non-negative integer and the value of an attribute, e.g., [value 2], is a float number. A line stands for a **test instance if [label] is 0** and a training instance otherwise. The label of a training instance can be any positive integer number.

Again, you may assume the test instances ([label] = 0) are at the end of the input file. Note that please do not assume the attribute names to start from 0 or to be consecutive integers, and please do not assume the class labels to start from 1 or to be consecutive integers.

    1 0:1.0 2:1.0 
    1 0:1.0 2:2.0 
    1 0:2.0 2:1.0 
    3 0:2.0 2:2.0 
    1 0:3.0 2:1.0 
    3 0:3.0 2:2.0 
    3 0:3.0 2:3.0 
    3 0:4.5 2:3.0 
    0 0:1.0 2:2.2 
    0 0:4.5 2:1.0


## Output Format and Sample
The output is the prediction on the test instances made by your KNN. Print the prediction for each test instance per line, following the order in the input file.
As an example the output of the toy example is as follows.

    1
    3