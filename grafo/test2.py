import utm
import pandas as pd


class Graph:

    def __init__(self, directed=True):

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
            print(f"node {key[0]}: {[(n[0][0], n[1]) for n in self.adj_list[key]]}")

    def findAllPaths(self, start, end, path=[], paths=[], cost=0):
        path = path + [start[0]]


        if start not in self.adj_list.keys():
            return None

        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.adj_list[start]:
            if node[0][0].name not in path:
                self.findAllPaths(start=node[0], end=end, path=path, paths=paths, cost=(cost + node[1]))

        return paths

    def findAllRealPaths(self, start, end, limit, path=[], paths=[], cost=0):
        path = path + [start[0]]

        if start not in self.adj_list.keys():
            return None

        if cost > limit:
            return None


        if start == end:
            pair = [path, cost]
            paths.append(pair)

        for node in self.adj_list[start]:
            if node[0][0] not in path:
                self.findAllRealPaths(start=node[0], end=end, limit=limit, path=path, paths=paths, cost=(cost + node[1]))

        return paths


    def visitAllNeighboursLimited(self, start, limit): 

        paths = []

        for node in self.adj_list.keys():

            paths_node = self.findAllRealPaths(start, node, limit)

            for path in paths_node:
                if path not in paths:
                    paths.append(path)

        return paths



def readCSV(f, graph):


    # Abre o csv usando apenas as colunas definidas
    data = pd.read_csv(f, sep="\t")[['FISICO_FONTE', 'FONTEX', 'FONTEY','FISICO_NO', 'NOX', 'NOY', 'COMPRIMENTO']]
    data = data.dropna() #limpa os valores vazios

    postes = []

    count = 0

    for i, row in data.iterrows(): #itera pelas linhas

        if count > 5:
            break;

        try:
            fonte = int(row['FISICO_FONTE']) #essa conversão elimina os postes com plaquetas não int
            nfonte = int(row['FISICO_NO'])
        except:
            continue



        p1 = ()
        p2 = ()


        x = float(row['FONTEX'].replace(',', '.')) # os postes tem seus numeros decimais separados por virgula =(
        y = float(row['FONTEY'].replace(',', '.'))

        nx = float(row['NOX'].replace(',', '.')) # os postes tem seus numeros decimais separados por virgula =(
        ny = float(row['NOY'].replace(',', '.'))

        cord = utm.to_latlon(x, y, 22, 'C')
        ncord = utm.to_latlon(nx, ny, 22, 'C')

        # p1[0] = fonte
        # p1[1] = cord[0]
        # p1[2] = cord[1]

        p1 = (fonte, cord[0], cord[1])
        p2 = (nfonte, ncord[0], ncord[1])
        #
        # p2[0] = nfonte
        # p2[1] = ncord[0]
        # p2[2] = ncord[1]


        print(p1, p2, row['COMPRIMENTO'])

        graph.addEdge(p1, p2, float(row['COMPRIMENTO'].replace(',', '.')))
        count += 1;

    return postes


graph = Graph(directed=False)


readCSV("postes.csv", graph)

print("")
graph.printAdjList()

print("")
print("")


x = graph.visitAllNeighboursLimited((139128, -30.131005246831297, -50.89506682860131), 999)

for i in x:
    print("")
    print(i )

