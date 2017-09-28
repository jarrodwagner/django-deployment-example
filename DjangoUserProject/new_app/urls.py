from django.conf.urls import url
from new_app import views

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^users/', views.users, name = 'users'),
    url(r'^addUser/', views.addUser, name = 'addUser')
]
