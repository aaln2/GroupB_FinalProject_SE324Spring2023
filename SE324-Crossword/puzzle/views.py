from django.shortcuts import render,redirect
#Parser
# Create your views here.
def puzzle(request):
    if request.method == "POST" and request.FILES['puzzle_words']:
        puzzle_words = request.FILES["puzzle_words"].read()
        arr = [i.decode().split(":") for i in puzzle_words.splitlines()]
        return render(request, "puzzle.html", {"puzzle": arr})
    else:
        return redirect("error")

def home(request):
    return render(request, "index.html")

def error(request):
    return render(request, "error.html")