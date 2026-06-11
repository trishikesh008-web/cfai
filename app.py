import random

def generate_graph(vertices):

    graph = [
        [0 for _ in range(vertices)]
        for _ in range(vertices)
    ]

    for i in range(vertices):
        for j in range(vertices):

            if i != j:
                graph[i][j] = random.randint(1, 20)

    return graph