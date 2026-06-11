def bellman_ford(graph, source):

    n = len(graph)

    dist = [float('inf')] * n

    dist[source] = 0

    start = time.perf_counter()

    for _ in range(n - 1):

        for u in range(n):

            for v in range(n):

                if (
                    graph[u][v]
                    and dist[u] != float('inf')
                    and dist[u] + graph[u][v] < dist[v]
                ):

                    dist[v] = dist[u] + graph[u][v]

    end = time.perf_counter()

    return round((end - start) * 1000, 5)