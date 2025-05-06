from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_trees,name='trees'),
    path('<int:tree_id>/', views.tree,name='test'),
    path('<int:tree_id>/<int:id>', views.tree_,name='test_'),
]
