""" 
Problem: https://www.urionlinejudge.com.br/judge/en/problems/view/1135
Dijkstra Algorithm: https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
"""
import sys

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}
        self.distance = sys.maxsize
        self.visited = False
        self.previous = None
   
    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight
    
    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return seft.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return f"{self.id} adjacent: [x.id for x in self.adjacent]"


class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0
        
    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        self.num_vertices += 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex
    
    def get_vertex(self, node):
        if node in self.vert_dict:
            return self.vert_dict[node]
        else:
            return None

    def add_edge(self, from_node, to_node, cost=0):
        if from_node not in self.vert_dict:
            self.add_vertex(from_node)
        if to_node not in self.vert_dict:
            self.add_vertex(to_node)

        self.vert_dict[from_node].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to_node].add_neighbor(self.vert_dict[from_node], cost)
    
    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self):
        return self.previous

    def shortest(self, path):
        '''make shortest path from v.previous'''
        if v.previous:
            path.append(v.previous.get_id())
            shortest(v.previous, path)
        return


def create_graph(anthills):
    graph = Graph()
    graph = create_vertices(graph, anthills)
    return graph

def create_vertices(graph, anthills):
    for a in range(1, anthills):
        graph.add_vertex(a)
    return graph

loop_condition = True

while loop_condition == True:
    data = input().split()
    if len(data) == 1:
        anthills_count = int(data[0])    
    if anthills_count == 0:
        break 

    graph = create_graph(anthills_count)
    print(graph.get_vertices())



    print(data)
