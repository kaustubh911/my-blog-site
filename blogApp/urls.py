from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^blog$', views.myBlog, name='myBlogPage')
]