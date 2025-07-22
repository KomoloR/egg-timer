from django.urls import path
from . import views

urlpatterns = [
    path('',views.timer , name='timer'),
    path('runny/', views.runny, name='runny'),
    path('soft/', views.soft, name='soft'),
    path('hard/',views.hard, name='hard'),
    path('over/',views.over, name ='over'),
]