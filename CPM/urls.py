from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("size/", views.get_diagram_info, name="size"),
    path("data/", views.activity_form, name="data"),
    path("create-form/", views.create_activity, name="create-activity"),
    path("generate", views.generate_diagram, name="generate-diagram"),
    path("delete_activity/<activity_id>", views.delete_activity, name="delete-activity"),
    path("upload/", views.generate_from_csv, name="upload"),
]