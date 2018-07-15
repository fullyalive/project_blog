# dojo/urls.py

from django.urls import path
from . import views

app_name = "dojo"

urlpatterns = [
    path("sum/<numbers>/", views.mysum, name="mysum"),
    path("hello/<name>/<age>", views.hello, name="hello"),
    path("list1/", views.post_list1, name="post_list1"),
    path("list2/", views.post_list2, name="post_list2"),
    path("list3/", views.post_list3, name="post_list3"),
    path("excel/", views.excel_download, name="excel_download")
]
