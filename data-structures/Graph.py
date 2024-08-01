# Graphs are a powerful tool for representing and analyzing
# complex relationships between objects or entities. They
# include vertices, which are the fundamental units of the
# graph, and edges, which are drawn or used to connect two
# nodes of the graph.

# Graphs are used to represent a wide range of relationships
# and data structures. They can be used to model and solve
# pathfinding, data clustering, network analysis, and
# machine learning problems. Their algorithms are often
# efficient and can be used to solve problems quickly, and
# they can be used to represent complex data structures in
# a simple and intuitive way.

# However, they can be difficult to understand. Creating
# and manipulating graphs can be computationally expensive,
# especially for very large and complex graphs. They can
# be difficult to design and implement correctly, and can
# be prone to bugs and errors. They can also be difficult
# to visualize and analyze, especially for very large or
# complex graphs.

def create_adjacency_matrix(graph):

    num_vertices = len(graph)

    adj_matrix = [[0] * num_vertices for _ in range(num_vertices)]

    for i in range(num_vertices):
        for j in range(num_vertices):
            if graph[i][j] == 1:
                adj_matrix[i][j] = 1
                adj_matrix[j][i] = 1

    return adj_matrix