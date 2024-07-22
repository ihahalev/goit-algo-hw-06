import matplotlib.pyplot as plt
import networkx as nx
# import networkx.algorithms.approximation as nx_app
import math

G = nx.random_geometric_graph(20, radius=0.4, seed=3)

if __name__ == "__main__":
    degrees = nx.degree(G)
    degree_centrality = nx.degree_centrality(G)
    closeness_centrality = nx.closeness_centrality(G)
    betweenness_centrality = nx.betweenness_centrality(G)
    print('Кількість вершин', G.number_of_nodes())
    print('Кількість ребер', G.number_of_edges())
    print('Граф сполучений (зв’язний)', nx.is_connected(G))
    print('Середній найкоротший шлях', nx.average_shortest_path_length(G))

    max = 0
    vertex = 0
    for degree in degrees:
        if degree[1] > max:
            max = degree[1]
            vertex = degree[0]
    vertexs = []
    for degree in degrees:
        if degree[1] == max:
            vertexs.append(degree[0])
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь {max}')
    max = 0
    vertex = 0
    for i in degree_centrality:
        if degree_centrality[i] > max:
            max = degree_centrality[i]
            vertex = i
    vertexs = []
    for i in degree_centrality:
        if degree_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь центральності {max}')
    max = 0
    vertex = 0
    for i in closeness_centrality:
        if closeness_centrality[i] > max:
            max = closeness_centrality[i]
            vertex = i

    vertexs = []
    for i in closeness_centrality:
        if closeness_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь близькості {max}')
    max = 0
    vertex = 0
    for i in betweenness_centrality:
        if betweenness_centrality[i] > max:
            max = betweenness_centrality[i]
            vertex = i
    vertexs = []
    for i in betweenness_centrality:
        if betweenness_centrality[i] == max:
            vertexs.append(i)
    print(f'{f'Вершини {vertexs} мають' if len(vertexs)>1 else f'Вершина {vertex} має'} найбільший ступінь посередництва {max}')

    # pos = nx.get_node_attributes(G, "pos")

    # Depot should be at (0,0)
    # pos[0] = (0.5, 0.5)

    # H = G.copy()

    # Calculating the distances between the nodes as edge's weight.
    # for i in range(len(pos)):
    #     for j in range(i + 1, len(pos)):
    #         dist = math.hypot(pos[i][0] - pos[j][0], pos[i][1] - pos[j][1])
    #         dist = dist
    #         G.add_edge(i, j, weight=dist)

    # cycle = nx_app.christofides(G, weight="weight")
    # edge_list = list(nx.utils.pairwise(cycle))

    # Draw closest edges on each node only
    nx.draw_networkx(
        G,
        # pos,
        edge_color="blue",
        width=0.5,
        with_labels=True,
        node_size=200)

    # Draw the route
    # nx.draw_networkx(
    #     G,
    #     pos,
    #     with_labels=True,
    #     edgelist=edge_list,
    #     edge_color="red",
    #     node_size=200,
    #     width=3,
    # )

    # print("The route of the traveller is:", cycle)
    plt.show()