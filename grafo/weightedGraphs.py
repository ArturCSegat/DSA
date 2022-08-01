""" class Graph_Matrix:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_directed = directed

        # Initialize the adjacency matrix
        # Create a matrix with `num_of_nodes` rows and columns # N x N columns  = O(n^2)
        self.m_adj_matrix = [[0 for column in range(num_of_nodes)] 
                            for row in range(num_of_nodes)]

    def add_edge(self, node1, node2, weight=1):
        self.m_adj_matrix[node1][node2] = weight

        if not self.m_directed:
            self.m_adj_matrix[node2][node1] = weight

    def print_adj_matrix(self):
        print(self.m_adj_matrix, "\n") """

class Graph_AdjList:
    def __init__(self, num_of_nodes, directed=True):
        self.m_num_of_nodes = num_of_nodes
        self.m_nodes = range(self.m_num_of_nodes)

        # Define the type of a graph
        self.m_directed = directed

        self.m_adj_list = {node: set() for node in self.m_nodes}      

    def addEdge(self, node1, node2, weight=1):
        self.m_adj_list[node1].add((node2, weight))
        
        if not self.m_directed:
        	self.m_adj_list[node2].add((node1, weight))
            
    def printAdjLIst(self):
        for key in self.m_adj_list.keys():
            print("node", key, ": ", self.m_adj_list[key])

    def findAllPaths(self, start, end, path=[], paths=[], cost=0):
        path = path + [start]

        
        
        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.m_adj_list[start]:
            if node[0] not in path:
                self.findAllPaths(start=node[0], end=end, path=path, paths=paths, cost=(cost + node[1]))
        
        return paths

    def findShortestPath(self, start, end, path=[], cost=0):
        """ path = path + [start]
            if start == end:
                return path
            if start not in self.m_adj_list:
                return None
            shortest = None
            for node in self.m_adj_list[start]:
                if node not in path:
                    newpath = find_shortest_path(node, end, path)
                    if newpath:
                        if shortest is None or len(newpath) < len(shortest):
                            shortest = newpath
            return shortest """

        path = path + [start]

        if start == end:
            return [path, cost]
        if start not in self.m_adj_list.keys():
            return None
        
        shortest = [None, 0] # None represents the shortest path and 0 the cost to perform it

        for node in self.m_adj_list[start]:
            if node[0] not in path:
                new_path = self.findShortestPath(node[0], end, path, (cost+node[1]))
                if new_path:
                    if shortest[0] is None or new_path[1] < shortest[1]:
                        shortest[0] = new_path[0]
                        shortest[1] = new_path[1]
        return shortest
    
    def findLongestPath(self, start, end, path=[], cost=0):
        path = path + [start]

        if start == end:
            return [path, cost]
        if start not in self.m_adj_list.keys():
            return None
        
        shortest = [None, 0] # None represents the shortest path and 0 the cost to perform it

        for node in self.m_adj_list[start]:
            if node[0] not in path:
                new_path = self.findShortestPath(node[0], end, path, (cost+node[1]))
                if new_path:
                    if shortest[0] is None or new_path[1] > shortest[1]:
                        shortest[0] = new_path[0]
                        shortest[1] = new_path[1]
        return shortest




""" graph = Graph_Matrix(5, False)

graph.add_edge(0, 0, 25)
graph.add_edge(0, 1, 5)
graph.add_edge(0, 2, 3)
graph.add_edge(1, 3, 1)
graph.add_edge(1, 4, 15)
graph.add_edge(4, 2, 7)
graph.add_edge(4, 3, 11)

graph.print_adj_matrix() """

graph2 = Graph_AdjList(5, False)


graph2.addEdge(0, 0, 25)
graph2.addEdge(0, 1, 5)
graph2.addEdge(0, 2, 3)
graph2.addEdge(1, 3, 1)
graph2.addEdge(1, 4, 15)
graph2.addEdge(4, 2, 7)
graph2.addEdge(4, 3, 11)
graph2.addEdge(2, 2, 2)

graph2.printAdjLIst()
print("")
print("Path between 2 and 3")
print("As g")
p = graph2.findAllPaths(2, 3)
print("All paths: ", p)
print("")
s = graph2.findShortestPath(2, 3)
print("Lowest cost path", s)
print("")
l = graph2.findLongestPath(2, 3)
print("Highest cost paht", l)
