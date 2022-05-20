from django.shortcuts import render, HttpResponseRedirect
from . forms import GroupeForm
from . import models

# Create your views here.

def formulaire(request):
        if request.method == "POST":
            form = GroupeForm(request)
            return render(request, "bibliotheque/groupedemetal/formulaire.html", {"form" : form})
        else :
            form = GroupeForm()
            id = ""
            return render(request, "bibliotheque/groupedemetal/formulaire.html", {"form" : form, "id":id})

def traitement(request):
    lform = GroupeForm(request.POST)
    if lform.is_valid():
        groupedemetal = lform.save()

        return HttpResponseRedirect('/groupedemetal/indexgroupedemetal/')
    else :
        return render(request, "bibliotheque/groupedemetal/formulaire.html", {"form": lform})

def index(request):
    liste = list(models.Groupedemetal.objects.all())
    return render(request,'bibliotheque/groupedemetal/index.html',{'liste' : liste})

def affiche(request, id):
    groupedemetal = models.Groupedemetal.objects.get( pk = id)
    liste = models.Groupedemetal.objects.filter(typedemetal_id = id)
    return render(request, 'bibliotheque/groupedemetal/affiche.html', {"groupedemetal" : groupedemetal, 'liste' : liste})

def update(request, id):
    groupedemetal = models.Groupedemetal.objects.get( pk = id)
    form = GroupeForm(groupedemetal.dico())
    return render(request, 'bibliotheque/groupedemetal/formulaire.html', {'form': form, 'id': id})

def updatetraitement(request, id):
    lform = GroupeForm(request.POST)
    if lform.is_valid():
        groupedemetal = lform.save(commit = False)
        groupedemetal.id = id
        groupedemetal.save()
        return HttpResponseRedirect('/groupedemetal/indexgroupedemetal/')
    else:
        return render(request, "bibliotheque/groupedemetal/formulaire.html", {"form": lform, "id": id})
def delete(request, id):
    groupedemetal = models.Groupedemetal.objects.get( pk=id )
    groupedemetal.delete()
    return HttpResponseRedirect('/groupedemetal/indexgroupedemetal/')
