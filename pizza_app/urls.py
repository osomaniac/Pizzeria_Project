from django.urls import path
from . import views

app_name = 'pizza_app'

urlpatterns = [
    path('',views.index, name='index'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('pizza/<int:pizza_id>/', views.pizza, name='pizza'),
    path('new_comment/<int:pizza_id>/', views.new_comment, name='new_comment'),
    path('edit_comment/<int:comment_id>/', views.edit_comment, name='edit_comment')
]