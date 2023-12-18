from django.urls import path
from .import views



urlpatterns = [
    path("", views.index,name="Index"),
    path("<int:id>", views.view_student,name="view_student"),
    path("create/", views.add_student,name="add_student"),
    path("edit/<int:id>/", views.edit,name="edit_student"),
    path("delete/<int:id>/", views.delete,name="delete"),


]