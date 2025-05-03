from django.urls import path, include
from .import views
urlpatterns = [
    path('', views.home, name='home'),
    path('habits/', views.add_habits, name='habit'),
    path('complete_h/<int:id>', views.complete_habit, name='complete_habit'),
    path('uncomplete_h/<int:id>', views.uncomplete_habit, name = 'uncomplete_habit'),
    path('quests/', views.add_quests, name='quest'),
    path('complete_q/<int:id>', views.complete_quest, name='complete_quest'),
    path('uncomplete_q/<int:id>', views.uncomplete_quest, name = 'uncomplete_quest'),
    path('edit_habit/<int:id>', views.edit_habits, name = 'edit_habit'),
    path('delete_habit/<int:id>', views.delete_habits, name = 'delete_habit'),
    path('reg',views.register,name='register'),
    path('log',views.login_,name='login'),
    path('logout',views.logout,name='logout'),
    path('api/habits/', views.HabitListCreateView.as_view(), name='habit_list'),
    path('api/habits/<int:pk>/', views.HabitDetailView.as_view(), name='habit_detail'),
]
