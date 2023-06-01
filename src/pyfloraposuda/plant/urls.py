from django.urls import path

from . import views


app_name = 'plant'

urlpatterns = [
    path('', views.plants, name='plants'),
    path('nova_biljka/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/brisanje/', views.delete, name='delete'),
    path('<int:pk>/promjena/', views.edit, name='edit'),
    
]