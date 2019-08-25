from django.urls import path
from Productos import views


urlpatterns = [

    path('agregar', views.add, name="add"),
    path('lista', views.list, name="list"),
    path('editar/<int:id>', views.edit, name="edit"),
    path('delete/<int:id>', views.delete, name="delete"),

]