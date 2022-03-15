from django.urls import path

from . import views
app_name ='basket'

urlpatterns = [
    path('b/', views.basket_summary, name='basket_summary'),
    path('a/', views.basket_add, name='basket_add'),
    path('d/', views.basket_delete, name='basket_delete'),
    path('u/', views.basket_update, name='basket_update'),
]
