import time

def dijkstra(graph, source):

    n = len(graph)

    dist = [float('inf')] * n

    visited = [False] * n

    dist[source] = 0

    start = time.perf_counter()

    for _ in range(n):

        min_dist = float('inf')
        u = -1

        for i in range(n):

            if not visited[i] and dist[i] < min_dist:

                min_dist = dist[i]
                u = i

        visited[u] = True

        for v in range(n):

            if (
                not visited[v]
                and graph[u][v]
                and dist[u] + graph[u][v] < dist[v]
            ):

                dist[v] = dist[u] + graph[u][v]

    end = time.perf_counter()

    return round((end - start) * 1000, 5)