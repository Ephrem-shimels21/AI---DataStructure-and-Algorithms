from collections import deque
import heapq
import math
import util
import random
import timeit

# class Node:
#     """
#     Node to represent city in hand
#     """

class Graph:
    """
    Graph class that defines a graph data structure
    """
    def __init__(self):
        self.graph = {}
        self.locations = {}
    
    def createNode(self, node):
        """
        Create a node in the graph
        """
        self.graph[node] = []
    
    def insertEdge(self, node_A, node_B, cost):
        """
        Insert Edge between node_A and node_B
        """
        # print("here is the cost",cost)
        if not node_A in self.graph:
            self.createNode(node_A)
        if not node_B in self.graph:
            self.createNode(node_B)
        
        self.graph[node_A].append((node_B, cost))
        self.graph[node_B].append((node_A, cost))
    
    def deleteEdge(self, node_A, node_B, cost):
        """
        delete edge between node node_A and node_B
        """
        self.graph[node_A].remove((node_B, cost))
        self.graph[node_B].remove((node_A, cost))

    def deleteNode(self, node_A):
        """
        delete node from graph
        """
        for node in self.graph:
            for neighbor in self.graph[node]:
                if neighbor[0] == node_A:
                    self.graph[node].remove(neighbor)
        
        del self.graph[node_A]


    def neighbours(self,nod):
        if nod in self.graph and self.graph[nod] != None:
            return self.graph[nod]
    
    # def generate_random_graph(n, p):
    #     graph = {}
    #     # nodes = list(range(n))
    #     for i in range(n):
    #         graph[i] = []
    #         for j in range(n):
    #             if i != j and random.random() < p:
    #                 graph[i].append(j)
    #     return graph
    
    def create_nodes(self,n):
        i = 0
        j = 0
        while i != n:
            x = random.randint(0,100)
            y  = random.randint(0,100)
            if (x,y) not in self.graph.keys():
                self.graph[(x,y)] = []
                i += 1
            j += 1
        print(j)
        return self.graph
        
    def generate_random_graph(self,n, p):
            graph = Graph()
            for i in range(1, n + 1):
                graph.locations[i] = (random.uniform(1.0, 100.0) , random.uniform(1.0, 100.0))
                for j in range(i + 1, n + 1):
                    if random.random() < p: 
                        graph.insertEdge(i, j, random.randrange(1, 150))
        
            return graph


