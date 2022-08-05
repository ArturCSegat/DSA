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

    def visitAllNeighboursLimited(self, node, limit, path=[], paths=[], cost=0, start=None):

        if start is None:
            start = node

        path.append(node[0])

        pair = (path, cost)

        if pair not in paths:
            paths.append(pair)
            return self.visitAllNeighboursLimited(node=start, start=start, limit=limit, path=[], paths=paths)

        for neighbour in self.adj_list[node]:

            if neighbour[0][0] not in path:

                if cost + neighbour[1] >= limit:
                    paths.append(pair)
                    return self.visitAllNeighboursLimited(node=start, start=start, limit=limit, path=[], paths=paths)

                return self.visitAllNeighboursLimited(node=neighbour[0], start=start, limit=limit, path=path, paths=paths, cost=(cost + neighbour[1]))

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


x = graph.visitAllNeighboursLimited(node=(139128, -30.131005246831297, -50.89506682860131), limit=999)

for i in x:
    print("")
    print(i )
