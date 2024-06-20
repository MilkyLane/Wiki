from django.urls import path

from . import views
app_Name = "wiki"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="title"),
    path("search/", views.search, name="search"),
    path("page/", views.newPage, name="newPage"),
    path("wiki/<str:title>", views.rand, name="rand"),
    path("edit/", views.edit, name="edit"),
    path("saveEdit/", views.saveEdit, name="saveEdit"),
    path("rand/", views.rand, name="rand")
]

