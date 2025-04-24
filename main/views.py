from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader, Template
from .forms import HabitForm
from .models import Habit
def home(request):
    t = loader.get_template('home.html')
    habits = Habit.objects.all()
    return render(request, 'home.html', context={'habits':habits})

def habits(request):
    habit_form = HabitForm()
    t = loader.get_template('add_habit.html')
    return render(request, 'add_habit.html',context={'form':habit_form})

def add_habits(request):
    if request.method == 'POST':
        form = HabitForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('home')
        else:
            form = HabitForm()
    return render(request, 'add_habit.html', context={'form':HabitForm()})

def complete_habit(request, id):
    if request.method == "POST":
        habit = get_object_or_404(Habit, id=id)
        habit.completed = True
        habit.save()
    return redirect('home')
    
# Create your views here.
