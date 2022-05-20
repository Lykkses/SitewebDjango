from django.urls import path
from . import views, typedemetal_views

urlpatterns = [
    # page pour les groupes de metal
    path('formulaire/', views.formulaire),
    path('traitement/', views.traitement),
    path('indexgroupedemetal/', views.index),
    path('affiche/<int:id>/', views.affiche),
    path('update/<int:id>/', views.update),
    path('updatetraitement/<int:id>/', views.updatetraitement),
    path('delete/<int:id>/', views.delete),
    # page pour les différents types de metal
    path('indextypedemetal/', typedemetal_views.index),
    path('', typedemetal_views.index),
    path('formulairetypedemetal/', typedemetal_views.formulaire),
    path('traitementtypedemetal/', typedemetal_views.traitement),
    path('affichetypedemetal/<int:id>/', typedemetal_views.affiche),
    path('deletetypedemetal/<int:id>/', typedemetal_views.delete),
    path('updatetypedemetal/<int:id>/', typedemetal_views.update),
    path('updatetraitementtypedemetal/<int:id>/', typedemetal_views.updatetraitement),

]