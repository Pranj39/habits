from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('habits/', views.add_habits, name='habit'),
    path('complete_h/<int:id>', views.complete_habit, name='complete_habit')
]
