from django import forms
from .models import Habit

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name','time_required', 'difficulty']
        widgets = {
            'name':forms.TextInput(),
            'time_required': forms.TimeInput(attrs={'type':'time'}),
            'difficulty':forms.NumberInput(attrs={'min':1,'max':10})
        }