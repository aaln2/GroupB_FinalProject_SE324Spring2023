from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError

# Parser

def create_maze(arr: list):
    last_item = len(arr) - 1
    maze = ""
    for k, row in enumerate(arr):
        maze += "<div>"
        for cell in row:
            if cell == 0:
                maze += "<div class='wall'></div>"
            elif k == 0 and cell == 1:
                maze += "<div class='door exit'></div>"
            elif k == last_item and cell == 1:
                maze += "<div class='door entrance hero'></div>"
            elif cell == 1:
                maze += "<div></div>"
        maze += "</div>"
    return maze


# Create your views here.
def maze(request):
    if request.method == "POST" and request.FILES.get("maze2d", False):
        maze2d = request.FILES["maze2d"].read()
        arr = [[int(x) for x in i.decode()] for i in maze2d.splitlines()]
        maze = create_maze(arr)
        return render(request, "maze.html", {"maze": maze})
    else:
        maze = "<h1 style='color:red'>insert valid maze</h1>"

    return render(request, "maze.html", {"maze": maze})


def home(request):
    return render(request, "index.html")
