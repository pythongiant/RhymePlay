from django.shortcuts import render,redirect
from . import forms 
import pronouncing
Rhyme=[]
points=0

def check(wrd1,wrd2):
    if wrd1 in wrd2:
        return True
    else:
        return False
# Create your views here.
def index(request):
    return render(request, "Rhyme/index.html", {})
def rhyme(request):
    global points
    rhymeForm=forms.Rhyme()
    print(Rhyme)
    Rhymes=[]
    for i in range(len(Rhyme)):
        Rhymes.append(Rhyme[i].replace(Rhyme[i].split()[-1],'')+"<span>"+str(Rhyme[i].split()[-1])+"</span>")
        rhyme=str(Rhyme[i].split()[-1])
        

            
        
    return render(request, "Rhyme/compGame.html", {"form":rhymeForm,"rhymes":Rhymes,"points":points})
    
def rhymeAction(request):
    rhymeForm=forms.Rhyme()
    print("SOmeone called me ?")
    if request.method == "POST":
        rhymeForm = forms.Rhyme(request.POST)
        if rhymeForm.is_valid():
           
            global points
            try:
                print("imp->"+rhymeForm.cleaned_data["rhyme"])
                if check(rhymeForm.cleaned_data["rhyme"].split()[-1],pronouncing.rhymes(Rhyme[len(Rhyme)-1].split()[-1])):
                    points+=1
                    print("added")
            except IndexError :
                print("FAL")
            Rhyme.append(rhymeForm.cleaned_data["rhyme"])
    return redirect("/compRhyme")
def mRhyme(request):
    return render(request, "Rhyme/multiGame.html", {})