from django.shortcuts import render,HttpResponse,redirect
from .models import Todo

# Create your views here.

def index(request):
    todos= Todo.objects.all()
    return render(request,"index.html",{"todos":todos})


def addTodo(request):
    if request.method== "GET":
        return redirect("/")
    else:
        titlee= request.POST.get("title")
        newTodo= Todo(title= titlee, completed= False)
        newTodo.save()
        return redirect("/")

def update(request,id):
    todo= Todo.objects.filter(id=id).first()
    todo.completed= not todo.completed
    todo.save()
    return redirect("/")

def delete(request,id):
    todo= Todo.objects.filter(id=id).first()
    todo.delete()
    return redirect("/")