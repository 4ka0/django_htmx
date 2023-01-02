from django.contrib import admin
from django.urls import path

from todo.views import todos, add_todo


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todos, name='todos'),
    path('add_todo', add_todo, name='add_todo'),
]
