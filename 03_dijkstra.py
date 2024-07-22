import networkx as nx
import math
graph = __import__('01_graph_analys')
G:nx.Graph = graph.G

def dijkstra(graph:nx.Graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph.nodes}
    distances[start] = 0
    unvisited = list(graph.nodes)

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        neighbors = graph[current_vertex]
        for neighbor, param in neighbors.items():
            distance = distances[current_vertex] + param['weight']

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances

if __name__ == "__main__":
    pos = nx.get_node_attributes(G, "pos")
    H = G.copy()

    # Calculating the distances between the nodes as edge's weight.
    for i in range(len(pos)):
        for j in range(i + 1, len(pos)):
            if H.has_edge(i,j):
                H[i][j]['weight'] = math.hypot(pos[i][0] - pos[j][0], pos[i][1] - pos[j][1])

    start = 0
    results = dijkstra(H, start)
    max = 0
    vertex = start
    for res in results.items():
        print(res)
        if res[1] > max:
            max = res[1]
            vertex=res[0]
    vertexs = []
    for res in results.items():
        if res[1] == max:
            vertexs.append(res[0])
    print(f"Найдовший шлях з вершини {start} до {f'вершин {vertexs}' if len(vertexs)>1 else f'вершини {vertex}'}, що складає {max}")
