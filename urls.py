from django.urls import path
from mainApp import views

urlpatterns = [
    path("mainApp/", views.home, name="mainApp"),
    path("student/<int:userId>/product/<int:productId>", views.add_vision)
]