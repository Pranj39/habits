from django import forms
from .models import Habit, Quest
from django.contrib.auth.forms import UserCreationForm
from skills.models import Tree


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

class HabitForm(forms.ModelForm):
    skills =  forms.ModelMultipleChoiceField(queryset=Tree.objects.none(),widget=forms.CheckboxSelectMultiple)
    class Meta:
        model = Habit
        fields = ['name','time_required', 'difficulty', 'reset_time', 'skills']
        widgets = {
            'name':forms.TextInput(),
            'time_required': forms.NumberInput(attrs={
                'class': 'form-input'
            }),
            'difficulty':forms.NumberInput(attrs={'max':'10','min':'1'}),
            'reset_time':forms.TimeInput(attrs={'type':'time'})
        }
    def __init__(self, *args, **kwargs):
       user = kwargs.pop('user', None)
       super().__init__(*args, **kwargs)
       if user:
           self.fields['skills'].queryset = Tree.objects.filter(user=user)

        
class QuestForm(forms.ModelForm):
    class Meta:
        model = Quest
        fields = ['name','time_required', 'difficulty']
        widgets = {
            'name':forms.TextInput(),
            'time_required': forms.NumberInput(attrs={
                'class': 'form-input'
            }),
            'difficulty':forms.NumberInput(attrs={'min':1,'max':10})
        }