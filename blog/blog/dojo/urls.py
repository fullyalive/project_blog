# dojo/urls.py

from django.urls import path
from . import views

app_name = "dojo"

urlpatterns = [
    path("sum/<x>/", views.mysum, name="mysum"),
    path("sum/<x>/<y>/", views.mysum, name="mysum"),
]
