from django.shortcuts import render,redirect
from .models import Curso
from django.contrib import messages
# Create your views here.
def index(request):
    cursosListados = Curso.objects.all()
    context = {"cursos":cursosListados}
    return render(request,'index.html', context)

def registrarCurso(request):
    codigo=request.POST['txtcodigo']
    nome=request.POST['txtnome']
    professor=request.POST['txtprofessor']
    creditos=request.POST['numcreditos']

    curso=Curso.objects.create(codigo=codigo,nome=nome,professor=professor,creditos=creditos)

    messages.success(request, 'Curso Cadastrado!')

    return redirect('/')


def excluirCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    curso.delete()
    messages.success(request, 'Curso Excluído!')
    return redirect('/')

def editarCurso(request,codigo):
    curso=Curso.objects.get(codigo=codigo)
    context={"curso":curso}
    return render(request, "editar.html", context)

def editandoCurso(request):
    codigo=request.POST['txtcodigo']
    nome=request.POST['txtnome']
    professor=request.POST['txtprofessor']
    creditos=request.POST['numcreditos'] 

    curso=Curso.objects.get(codigo=codigo)
    curso.nome=nome
    curso.professor=professor
    curso.creditos=creditos

    curso.save()
    messages.success(request, 'Curso Alterado!')
    return redirect('/')

