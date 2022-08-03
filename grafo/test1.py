class G:

    def __init__(self, name, guitarra, banda=None):

        self.name = name
        self.guitarra = guitarra
        self.banda = banda

    def tocar(self):
        print("0 3 5, 0 3 65, 0 3 5 3 0")


class Graph:
    def __init__(self, num_of_nodes, directed=True):
        self.num_of_nodes = num_of_nodes

        # Define the type of a graph
        self.directed = directed

        self.adj_list = {}

    def addEdge(self, node1, node2, weight=1):
        if node1 in self.adj_list.keys():
             self.adj_list[node1].add((node2, weight))

        else:
             self.adj_list[node1] = set()
             self.adj_list[node1].add((node2, weight))




        if self.directed == False:
             if node2 in self.adj_list.keys():
                 self.adj_list[node2].add((node1, weight))

             else:
                 self.adj_list[node2] = set()
                 self.adj_list[node2].add((node1, weight))


    def printAdjList(self):
        for key in self.adj_list.keys():
            print(f"node {key.name}: {[(n[0].name, n[1]) for n in self.adj_list[key]]}")

    def findAllPaths(self, start, end, path=[], paths=[], cost=0):
        path = path + [start.name]


        if start not in self.adj_list.keys():
            return None

        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.adj_list[start]:
            if node[0].name not in path:
                self.findAllPaths(start=node[0], end=end, path=path, paths=paths, cost=(cost + node[1]))

        return paths


    def findAllRealPaths(self, start, end, path=[], paths=[], cost=0):
        path = path + [start.name]

        if start not in self.adj_list.keys():
            return None

        if cost > 15:
            return None


        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.adj_list[start]:
            if node[0].name not in path:
                self.findAllRealPaths(start=node[0], end=end, path=path, paths=paths, cost=(cost + node[1]))

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
                    if shortest[0] is None or new_path[1] > shortest[1]:
                        shortest[0] = new_path[0]
                        shortest[1] = new_path[1]
        return shortest






graph = Graph(5, False)


a1 = G("Frusciante", "strat", "rhcp")
a2 = G("Hendrix", "strat")
a3 = G("Gilmour", "strat", "Pink Floyd")
a4 = G("Page", "les paul", "Led Zepellin")
a5 = G("Jober", "strat", "Riachuelo")
a6 = G("Vaughan", "strat")
a7 = G("Joe Pass", "emperor")
a8 = G("Kfh", "ibanez", "ch")


graph.addEdge(a2, a6, 2)
graph.addEdge(a6, a1, 5)
graph.addEdge(a1, a2, 5)
graph.addEdge(a2, a4, 12)
graph.addEdge(a5, a3, 1)
graph.addEdge(a6, a3, 13)
graph.addEdge(a5, a4, 7)
graph.addEdge(a8, a5, 0.5)
graph.addEdge(a8, a7, 15)
graph.addEdge(a1, a8, 3)
graph.addEdge(a7, a2, 9)
graph.addEdge(a4, a7, 8)
graph.addEdge(a8, a4, 5)


graph.printAdjList()

print("")
print(graph.findAllPaths(a8, a4))
print("")
print(graph.findAllRealPaths(a8, a4))
