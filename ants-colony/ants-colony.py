""" 
Problem: https://www.urionlinejudge.com.br/judge/en/problems/view/1135
Dijkstra Algorithm: https://www.bogotobogo.com/python/python_Dijkstras_Shortest_Path_Algorithm.php
"""
import sys
import heapq

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
        return self.id

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

        self.vert_dict[from_node].add_neighbor(self.vert_dict[to_node], cost)
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

def dijkstra(aGraph, start, target):
    start.set_distance(0)

    #unvisited_queue = [(v.get_distance(), v) for v in aGraph]
    unvisited_queue = [v.get_distance() for v in aGraph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        uv = heapq.heappop(unvisited_queue)
        current = uv[1]
        current.set_visited()

        for next_node in current.adjacent:
            if next_node.visited:
                continue
            new_dist = current.get_distance() + current.get_weight(next_node)
            
            if new_dist < next_node.get_distance():
                next_node.set_distance(new_dist)
                next_node.set_previous(current)
                print(f'updated: current = {current.get_id()} next = {next_node.get_id()} new_dist = {next_node.get_distance()}')
            else:
                print(f'not updated: current = {current.get_id()} next = {next_node.get_id()} new_dist = {next_node.get_distance()}')

        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        unvisited_queue = [(v.get_distance(), v) for v in aGraph if not v.visited]
        heapq.heapify(unvisited_queue)


def create_graph(anthills):
    graph = Graph()
    graph = create_vertices(graph, anthills)
    return graph

def create_vertices(graph, anthills):
    for a in range(1, anthills):
        graph.add_vertex(a)
    return graph

def create_connections(graph, anthills):
    for from_node in range(1, anthills):
        to_node, distance = input().split()
        to_node = int(to_node)
        distance = int(distance)

        graph.add_edge(from_node, to_node, distance)
    return graph




loop_condition = True

while loop_condition == True:
    print('====================================================')
    anthills = int(input())    
    if anthills == 0:
        break 

    graph = create_graph(anthills)
    graph = create_connections(graph, anthills)

    #print(graph.get_vertices())

    for v in graph:
        for w in v.get_connections():
            vid = v.get_id()
            wid = w.get_id()
            print(f'{vid}, {wid}, {v.get_weight(w)}')
    
    queue_count = int(input())
    for q in range(queue_count):
        from_node, to_node = input().split()
        from_node = graph.get_vertex(int(from_node))
        to_node = graph.get_vertex(int(to_node))
        dijkstra(graph, from_node, to_node)

        target = g.get_vertex(to_node)
        path = [target.get_id()]
        shortest(target, path)
        print(f'shortest path: path')
