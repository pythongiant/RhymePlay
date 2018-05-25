from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "Rhyme/index.html", {})
def rhyme(request):
    return render(request, "Rhyme/compGame.html", {})

def mRhyme(request):
    return render(request, "Rhyme/multiGame.html", {})