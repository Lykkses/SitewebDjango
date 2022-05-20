from django.shortcuts import render, HttpResponseRedirect
from . forms import MetalForm
from . import models



def formulaire(request):
    if request.method == "POST":
        form = MetalForm(request)
        return render(request, "bibliotheque/typedemetal/formulaire.html", {"form": form})
    else:
        form = MetalForm()
        id=""
        return render(request, "bibliotheque/typedemetal/formulaire.html", {"form": form ,"id":id})


def traitement(request):
    lform = MetalForm(request.POST)
    if lform.is_valid():
        lform.save()
        return HttpResponseRedirect('/groupedemetal/indextypedemetal/')
    else:
        return render(request, "bibliotheque/typedemetal/formulaire.html", {"form": lform})


def index(request):
    liste = list(models.Typedemetal.objects.all())
    return render(request, 'bibliotheque/typedemetal/index.html', {'liste': liste})


def affiche(request, id):
    typedemetal = models.Typedemetal.objects.get(pk=id)
    liste = list(models.Groupedemetal.objects.filter(typedemetal=typedemetal))
    return render(request, 'bibliotheque/typedemetal/affiche.html', {"typedemetal": typedemetal,"liste":liste})


def update(request, id):
    typedemetal = models.Typedemetal.objects.get(pk=id)
    form = MetalForm(typedemetal.dico())
    return render(request, 'bibliotheque/typedemetal/formulaire.html', {'form': form, 'id': id})


def updatetraitement(request, id):
    lform = MetalForm(request.POST)
    if lform.is_valid():
        typedemetal = lform.save(commit=False)
        typedemetal.id = id
        typedemetal.save()
        return HttpResponseRedirect('/groupedemetal/indextypedemetal/')
    else:
        return render(request, "bibliotheque/typedemetal/formulaire.html", {"form": lform, "id": id})


def delete(request, id):
    typedemetal = models.Typedemetal.objects.get(pk=id)
    typedemetal.delete()
    return HttpResponseRedirect('/groupedemetal/indextypedemetal/')