from django.shortcuts import render,redirect
from .models import Tree, Node
from .forms import NodeForm, TreeForm
from .serializers import TreeSerializer, NodeSerializer
from rest_framework import generics,permissions
from django.contrib.auth.decorators import login_required
from rest_framework.authtoken.models import Token
import json
# Create your views here.


class TreeListCreateView(generics.ListCreateAPIView):
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tree.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class TreeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TreeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Tree.objects.filter(user=self.request.user)

class NodeListCreateView(generics.ListCreateAPIView):
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Node.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



class NodeDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = NodeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Node.objects.filter(user=self.request.user)
    
    def perform_update(self, serializer):
        instance = serializer.save()

        tree = instance.tree
        tree.structure = tree.root_node.get_c()
        tree.save()

@login_required
def tree_(request, tree_id, id):
    parent_node = Node.objects.filter(id=id).first()
    tree = Tree.objects.filter(id=tree_id).first()
    if request.method == "POST":
        node = Node(name=request.POST['name'], time_required= int(request.POST['time_required']), difficulty=int(request.POST['difficulty']), parent=parent_node, tree=tree, user=request.user)
        node.save()
        node.tree.structure = node.tree.root_node.get_c()
        node.tree.save()
        return redirect('edit_tree', tree_id=tree_id)
    return render(request,'skills/edit_tree.html', context={'nodes':Node.objects.all(),'tree_id':tree_id,'j':tree.structure,'token':Token.objects.filter(user=request.user).first().key})

@login_required
def display(request, tree_id):
    tree = Tree.objects.filter(id=tree_id).first()
    return render(request,'skills/tree.html', context={'nodes':Node.objects.all(),'tree_id':tree_id,'j':tree.structure,'token':Token.objects.filter(user=request.user)})

@login_required
def tree(request, tree_id):
    tree = Tree.objects.filter(id=tree_id).first()
    if tree.node.all():
        nodes = tree.node.all()
    else:
        node = Node(tree=tree, name=tree.name, user=request.user)
        tree.root_node = node
        node.root_node = True
        node.activated = True
        node.save()
        tree.structure = node.get_c()
        tree.save()
        nodes = tree.node.all()
    
    return render(request,'skills/edit_tree.html', context={'nodes':nodes,'tree_id':tree_id,'j':json.dumps(tree.structure),'tree':tree.node,'token':Token.objects.filter(user=request.user).first().key})

@login_required
def create_trees(request):
    
    if request.method == 'POST':
        form = TreeForm(request.POST)
        if form.is_valid():
            instance = form.instance
            instance.user = request.user
            instance.save()
            form.save()
            return redirect('trees')
        else:
            print(form.errors)
            return render(request,'skills/skills.html',context={'trees':Tree.objects.filter(user=request.user),'token':Token.objects.filter(user=request.user)})
    return render(request,'skills/skills.html',context={'trees':Tree.objects.filter(user=request.user),'token':Token.objects.filter(user=request.user)})

@login_required
def delete_trees(request, tree_id):

        tree = Tree.objects.filter(id=tree_id)
        tree.delete()
        return redirect('trees')
   

def edit_nodes(request, node_id):
    node = Node.objects.filter(id=node_id).first()
    if request.method == "POST":
        node_form = NodeForm(request.POST, instance=node)
        if node_form.is_valid():
            node_form.save()
            node.tree.structure = node.tree.root_node.get_c()
            if node.root_node == True:
                node.tree.name = request.POST['name']
            node.tree.save()
            return redirect('edit_tree', tree_id=node.tree.id)
        else:
            return render(request, 'skills/edit_node.html',{'node_form': node_form,'node':node})
    else:
        node_form = NodeForm(instance=node)
        return render(request,'skills/edit_node.html', {'node':node,'node_form':node_form})
        
