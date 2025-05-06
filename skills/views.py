from django.shortcuts import render,redirect
from .models import Tree, Node
import json
# Create your views here.

def tree_(request, tree_id, id):
    parent_node = Node.objects.filter(id=id).first()
    tree = Tree.objects.filter(id=tree_id).first()
    if request.method == "POST":
        node = Node(name=request.POST['name'], parent=parent_node, tree=tree)
        node.save()
        return redirect('test', tree_id=tree_id)
    return render(request,'test.html', context={'nodes':Node.objects.all(),'tree_id':tree_id})


def tree(request, tree_id):
    tree = Tree.objects.filter(id=tree_id).first()
    if tree.node.all():
        nodes = tree.node.all()
    else:
        node = Node(tree=tree)
        node.save()
        nodes = tree.node.all()
    
    return render(request,'test.html', context={'nodes':nodes,'tree_id':tree_id,'j':json.dumps(nodes.all().first().get_c()),'tree':tree.node})

def create_trees(request):

    if request.method == 'POST':
        tree = Tree(name=request.POST['tree_name'], user = request.user)
        tree.save()
        return redirect('trees')
    return render(request,'skills.html',context={'trees':Tree.objects.all()})