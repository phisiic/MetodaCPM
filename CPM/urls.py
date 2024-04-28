from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("size/", views.get_diagram_info, name="size"),
    path("data/", views.activity_form, name="data")
]