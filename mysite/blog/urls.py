from django.urls import  path
from . import views

app_name = "blog"
urlpatterns = [
    path("",views.index,name="index"),
    path("post/<int:post_id>", views.details, name="details"),
    path("post/old_url", views.old_url_redirect, name="old url redirect"),
    path("post/new_url", views.new_url, name="new_url")
]