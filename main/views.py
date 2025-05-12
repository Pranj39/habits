from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.template import loader, Template
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import HabitForm, MyUserCreationForm, QuestForm
from .models import Habit, Quest
from .serializers import HabitSerializer, UserProfileSerializer
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token



class HabitListCreateView(generics.ListCreateAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class HabitDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = HabitSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)


@login_required
def home(request):
    habits = Habit.objects.filter(user = request.user)
    com_habits = Habit.objects.filter(completed= True, user=request.user)
    quests = Quest.objects.filter(user= request.user)
    com_quests = Quest.objects.filter(completed=True, user = request.user)
    return render(request, 'main/home.html', context={'habits':habits, 'c_habits':com_habits,'quests':quests,'c_quests':com_quests})


@login_required
def add_habits(request):
    if request.method == 'POST':
        form = HabitForm(request.POST, user=request.user)
        if form.is_valid():

            instance = form.save()
            instance.user = request.user
            instance.save()
            return redirect('home')
        else:
            form = HabitForm(user=request.user)
    return render(request, 'main/add_habit.html', context={'form':HabitForm(user=request.user)})

def edit_habits(request, id):
    habit = get_object_or_404(Habit, id=id)
    if request.method == 'POST':
        form = HabitForm(request.POST, instance=habit)        
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = HabitForm(instance=habit)

    return render(request, 'main/edit_habit.html', {
        'form': form,
        'habit': habit,
    })



@login_required
def add_quests(request):
    if request.method == 'POST':
        form = QuestForm(request.POST)
        if form.is_valid:

            instance = form.save()
            instance.user = request.user
            instance.save()
            return redirect('home')
        else:
            form = QuestForm()
            
    return render(request, 'main/add_quest.html', context={'form':QuestForm()})

def complete_habit(request, id):

    if request.method == "POST":
        habit = get_object_or_404(Habit, id=id)
        habit.completed = True
        habit.user.profile.exp += habit.get_exp()
        habit.user.profile.level_up()
        habit.user.profile.save()
        print(habit.user.profile.exp)
        for skill in habit.skills.all():
            skill.exp += habit.exp_reward
            skill.skill_points += habit.exp_reward
            skill.save()
        habit.save()
    return redirect('home')


def delete_habits(request, id):
    
    habit = get_object_or_404(Habit, id=id)
    habit.delete()
    return redirect('home')

def uncomplete_habit(request, id):
    if request.method == "POST":
        habit = get_object_or_404(Habit, id=id)
        habit.completed = False
        habit.user.profile.exp -= habit.get_exp()
        habit.user.profile.level_down()
        habit.user.profile.save()
        print('hello')
        for skill in habit.skills.all():
            skill.exp -= habit.get_exp()
            skill.skill_points -= habit.get_exp()
            skill.save()
            
        habit.save()
    return redirect('home')

def complete_quest(request, id):

    if request.method == "POST":
        quest = get_object_or_404(Quest, id=id)
        quest.completed = True
        quest.user.profile.exp += quest.get_exp()
        quest.user.profile.level_up()
        quest.user.profile.save()
        print(quest.user.profile.exp)
        quest.save()
    return redirect('home')

def uncomplete_quest(request, id):
    if request.method == "POST":
        quest = get_object_or_404(Quest, id=id)
        quest.completed = False
        quest.user.profile.exp -= quest.get_exp()
        quest.user.profile.level_down()
        quest.user.profile.save()
        quest.save()
    return redirect('home')

def register(request):
    
    if request.method == "POST":
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    return render(request, 'main/register.html', context={'form':MyUserCreationForm})

def login_(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)  
            token, created = Token.objects.get_or_create(user=user)
            return redirect('home')  
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})
    
    
def logout(request):
    auth_logout(request)
    return redirect('home')
            
# Create your views here.
