class Person:

    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height


class Graph:

    def __init__(self, num_nodes, directed=True, base=[]):
        self.base = base
        self.num_nodes = num_nodes
        self.m_nodes = range(0, num_nodes) 

        self.directed = directed

        self.adj_list = {self.base[n]: set() for n in self.m_nodes}
    
    def addEdge(self, node1, node2, weight=1):
        self.adj_list[node1].add((node2, weight))

        if self.directed == False:
           self.adj_list[node2].add((node1, weight))

    def printAdjList(self):
        for key in self.adj_list.keys():
            print(f"node {key.name}: {self.adj_list[key]}")

    def findAllPaths(self, start, end, path=[], paths=[], cost=0):

        path.append(start)
        if start not in self.adj_list.keys():
            return None
        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.adj_list[start]:
            if node[0] not in path:
                self.findAllPaths(start=node[0], end=end, path=path, paths=paths, cost=(cost + node[1]))
        
        return paths

    def findShortestPath(self, start, end, path=[], cost=0):
        path = path + [start]

        if start == end:
            return [path, cost]
        if start not in self.adj_list.keys():
            return None
        
        shortest = [None, 0] # None represents the shortest path and 0 the cost to perform it

        for node in self.adj_list[start]:
            if node[0] not in path:
                new_path = self.findShortestPath(node[0], end, path, (cost+node[1]))
                if new_path:
                    if shortest[0] is None or new_path[1] < shortest[1]:
                        shortest[0] = new_path[0]
                        shortest[1] = new_path[1]
        return shortest
    
    def findLongestPath(self, start, end, path=[], cost=0):
        path.append(start)

        if start == end:
            return [path, cost]
        if start not in self.adj_list.keys():
            return None
        
        longest = [None, 0] # None represents the longest path and 0 the cost to perform it

        for node in self.adj_list[start]:
            if node[0] not in path:
                new_path = self.findLongestPath(node[0], end, path, (cost+node[1]))
                if new_path:
                    if longest[0] is None or new_path[1] > longest[1]:
                        longest[0] = new_path[0]
                        longest[1] = new_path[1]
        return longest
    




p0 = Person("Artur", 15, 3.5)
p1 = Person("Paulo", 16, 1.75)
p2 = Person("Pedro", 17, 1.8)
p3 = Person("João", 18, 1.5)
p4 = Person("Fulano", 19, 1.53)
p5 = Person("Ciclano", 20, 1.87)
p6 = Person("Beltrano", 10, 1.64)

people = [p0, p1, p2, p3, p4, p5, p6]

graph = Graph(7, False, people)

graph.addEdge(p0, p1, 5)
graph.addEdge(p2, p1, 3)
graph.addEdge(p3, p4, 1)
graph.addEdge(p6, p3, 9)
graph.addEdge(p5, p6, 1)
graph.addEdge(p1, p4, 3)
graph.addEdge(p3, p2, 7)
graph.addEdge(p2, p5, 4)
graph.addEdge(p0, p6, 2)
graph.addEdge(p2, p3, 5)


graph.printAdjList()
print("")
x = graph.findAllPaths(p0, p2)
print(x)
print("")
y = graph.findShortestPath(p0, p2)
print(y)
print("")
z= graph.findLongestPath(p0,p2)
print(z)

print("")

print("caminho mais curto")
print([p.name for p in y[0]] + [y[1]])
print("caminho mais longo")
print([p.name for p in z[0]] + [z[1]])

