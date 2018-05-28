from django.shortcuts import render,redirect
from . import forms 
import pronouncing
Rhyme=[]

# Create your views here.
def index(request):
    return render(request, "Rhyme/index.html", {})
def rhyme(request):
    rhymeForm=forms.Rhyme()
    print(Rhyme)
    Rhymes=[]
    for i in Rhyme:
        Rhymes.append(i.replace(i.split()[-1],'')+"<span>"+str(i.split()[-1])+"</span>")
    return render(request, "Rhyme/compGame.html", {"form":rhymeForm,"rhymes":Rhymes})
    
def rhymeAction(request):
    rhymeForm=forms.Rhyme()
    print("SOmeone called me ?")
    if request.method == "POST":
        rhymeForm = forms.Rhyme(request.POST)
        if rhymeForm.is_valid():
            Rhyme.append(rhymeForm.cleaned_data["rhyme"])

    return redirect("/compRhyme")
def mRhyme(request):
    return render(request, "Rhyme/multiGame.html", {})