from django.urls import path
from index import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu', views.menu, name='menu'),
    path('events', views.events, name='events')
]
