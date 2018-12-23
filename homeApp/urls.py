from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home$', views.myHome, name='myHomePage'),
    url(r'^contact$', views.myContact, name='myContactPage')
]