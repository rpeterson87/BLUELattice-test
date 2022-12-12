from django.urls import path
from .import views

# This is for routes in the app
urlpatterns = [
    path("", views.Home.as_view(), name="home" )
]
