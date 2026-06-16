from flask import request

@app.route("/", methods=["GET", "POST"])
def index():

    result = {}

    if request.method == "POST":

        vertices = int(request.form["vertices"])

        graph = generate_graph(vertices)

        result = {

            "dijkstra_time":
                dijkstra(graph, 0),

            "bellman_time":
                bellman_ford(graph, 0)
        }

    return render_template(
        "index.html",
        result=result
    )