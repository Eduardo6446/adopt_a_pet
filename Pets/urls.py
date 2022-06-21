from django.urls import path

from . import views

app_name = 'Pets'

urlpatterns = [
    path("", views.index, name="index")
]
