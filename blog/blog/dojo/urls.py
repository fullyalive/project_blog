# dojo/urls.py

from django.urls import path
from . import views

app_name = "dojo"

urlpatterns = [
    path("sum/<numbers>/", views.mysum, name="mysum"),
    path("hello/<name>/<age>", views.hello, name="hello"),
]
