from django import forms
from .models import Node, Tree

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['name', 'difficulty', 'time_required']
        