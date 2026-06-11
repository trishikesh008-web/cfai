# app.py
# Dijkstra vs Bellman-Ford Comparison using Flask

from flask import Flask, render_template, request
import random
import time

app = Flask(__name__)

# Generate weighted graph
def generate_graph(vertices):

    graph = [[0 for _ in range(vertices)] for _ in range(vertices)]

    for i in range(vertices):
        for j in range(vertices):

            if i != j:
                graph[i][j] = random.randint(1, 20)

    return graph


# Dijkstra Algorithm
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

    return {
        "distance": dist[n - 1],
        "time": round((end - start) * 1000, 5)
    }


# Bellman Ford Algorithm
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

    return {
        "distance": dist[n - 1],
        "time": round((end - start) * 1000, 5)
    }


@app.route("/", methods=["GET", "POST"])
def index():

    result = {}

    if request.method == "POST":

        vertices = int(request.form["vertices"])

        graph = generate_graph(vertices)

        dijkstra_result = dijkstra(graph, 0)

        bellman_result = bellman_ford(graph, 0)

        result = {

            "vertices": vertices,

            "dijkstra_time": dijkstra_result["time"],

            "bellman_time": bellman_result["time"],

            "dijkstra_distance": dijkstra_result["distance"],

            "bellman_distance": bellman_result["distance"]

        }

    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)