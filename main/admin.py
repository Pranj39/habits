from django.contrib import admin
from .models import Habit, UserProfile

# Register your models here.
admin.site.register(Habit)
admin.site.register(UserProfile)