from celery import shared_task
from .models import Habit
from datetime import datetime, timedelta

@shared_task
def reset_time():
    Habit.objects.all().update(reset=True)

@shared_task
def reset_daily_habits():
    for habit in Habit.objects.all():
        if habit.time:
            if datetime.now().time() > habit.time and habit.reset:
                habit.completed = False
                habit.reset = False
                habit.save()
                print(habit.name)
                print('true')

