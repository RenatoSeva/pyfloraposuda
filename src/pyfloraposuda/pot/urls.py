from django.urls import path

from . import views


app_name = 'pot'

urlpatterns = [
    path('', views.pots, name='pots'),
    path('nova_posuda/', views.new, name='new'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/brisanje/', views.delete, name='delete'),
    path('<int:pk>/promjena/', views.edit, name='edit'),
]