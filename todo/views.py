from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Todo


def todos(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todos.html', {'todos': todos})


"""
The @require_http_methods decorator:
Used to restrict access to views based on the request method. Below it is used
to restrict access to the add_todo view to requests made using the POST method.
A 'HttpResponseNotAllowed' is returned if this kind of condition is not met.

The empty second value on line 28 below:
title = request.POST.get('title', '')
POST.get('key')では、存在しないキーを指定したときはNoneが返されます。
POST.get('key', 'default')のように第二引数を設定すると、キーが存在しなかったときに、
設定した値をデフォルト値として返してくれます。このため、キーが存在しなくてもエラーが発生しません。
"""


@require_http_methods(['POST'])
def add_todo(request):
    todo = None
    title = request.POST.get('title', '')
    if title:
        todo = Todo.objects.create(title=title)
    return render(request, 'todo/partials/todo.html', {'todo': todo})


@require_http_methods(['PUT'])
def update_todo(request, pk):
    todo = Todo.objects.get(pk=pk)
    todo.is_done = True
    todo.save()
    return render(request, 'todo/partials/todo.html', {'todo': todo})
