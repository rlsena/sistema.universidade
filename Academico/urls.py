from . import views
from django.urls import path

urlpatterns = [
    path('',views.index,name='index'),
    path('registrarCurso/',views.registrarCurso,name='novoCurso'),
    path('excluirCurso/<codigo>',views.excluirCurso,name='excluir'),
    path('editarCurso/<codigo>',views.editarCurso,name='editar'),
    path('editandoCurso/',views.editandoCurso,name='editando'),


]