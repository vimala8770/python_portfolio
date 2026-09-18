from django.urls import path

from . import views

app_name = "portfolio"

urlpatterns = [
    path("", views.home, name="home"),
    path("resume/", views.download_resume, name="resume"),
]
