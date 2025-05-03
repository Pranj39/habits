from django import forms
from .models import Habit, Quest
from django.contrib.auth.forms import UserCreationForm


class MyUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'email')

class HabitForm(forms.ModelForm):
    class Meta:
        model = Habit
        fields = ['name','time_required', 'difficulty', 'reset_time']
        widgets = {
            'name':forms.TextInput(),
            'time_required': forms.NumberInput(attrs={
                'class': 'form-input'
            }),
            'difficulty':forms.NumberInput(attrs={'min':1,'max':10}),
            'reset_time':forms.TimeInput(attrs={'type':'time'})
        }

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