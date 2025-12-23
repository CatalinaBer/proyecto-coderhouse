from django.urls import path
from estudio.views import *


urlpatterns = [
    path("", home, name="home"),
]