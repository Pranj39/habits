from django.urls import path
from . import views
urlpatterns = [
    path('', views.create_trees,name='trees'),
    path('<int:tree_id>/', views.tree,name='edit_tree'),
    path('<int:tree_id>/<int:id>/', views.tree_,name='edit_tree_'),
    path('<int:tree_id>/display', views.display,name='display'),
    path('delete/<int:tree_id>/', views.delete_trees,name='delete_tree'),
    path('edit_node/<int:node_id>/', views.edit_nodes,name='edit_node'),
    path('api/skills/', views.TreeListCreateView.as_view(), name='tree_list'),
    path('api/skills/<int:pk>', views.TreeDetailView.as_view(), name='tree_detail'),
    path('api/nodes/', views.NodeListCreateView.as_view(), name='node_list'),
    path('api/nodes/<int:pk>', views.NodeDetailView.as_view(), name='node_detail'),
]
