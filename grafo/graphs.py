#supossed to represent simple graph

graph = {
0: [1, 2],
1: [0, 3, 6],
2: [0, 3, 6],
3: [1, 2, 4, 5],
4: [3],
5: [3],
6: [2, 1]}

def find_all_paths(graph, start, end, path=[], paths=[]):
    path = path + [start]

    
    
    if start == end:
        paths.append(path)

    for node in graph[start]:
        if node not in path:
            find_all_paths(graph, node, end, path, paths)
    
    return paths



def find_shortest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_shortest_path(graph, node, end, path)
            if newpath:
                if shortest is None or len(newpath) < len(shortest):
                    shortest = newpath
    return shortest

def find_longest_path(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return path
    if start not in graph:
        return None
    longest = None
    for node in graph[start]:
        if node not in path:
            newpath = find_longest_path(graph, node, end, path)
            if newpath:
                if longest is None or len(newpath) > len(longest):
                    longest = newpath
    return longest


print("All paths: ", find_all_paths(graph, 3, 6))
print("Shortest path: ", find_shortest_path(graph, 3, 6))
print("Longest path: ", find_longest_path(graph, 3, 6))
