from sanic import Sanic
from sanic.response import json

app = Sanic("VercelPythonApp")

@app.route("/")
async def read_root(request):
    return json({"Hello": "World"})

@app.route("/<full_path:path>")
async def read_anything(request, full_path):
    return json({"path": full_path})
