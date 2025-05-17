from django import forms
from .models import Node, Tree

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['name', 'difficulty', 'time_required']
    
class TreeForm(forms.ModelForm):
    class Meta:
        model = Tree
        fields = ['name']
        