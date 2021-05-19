from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("stream/",views.stream,name="stream"),
    path("stop/",views.stop,name="stop")
]
