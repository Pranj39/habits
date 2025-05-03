from celery import shared_task
from django.utils import timezone
from .models import Habit
import pytz
@shared_task
def reset_habits_by_time():

    print(timezone.get_current_timezone_name())
    for habit in Habit.objects.all():
        timezone.activate(habit.user.profile.timezone)
    
    

    now = timezone.localtime().time().replace(second=0, microsecond=0)
    h = Habit.objects.filter(needs_reset=True, completed=True)
    print(h)
    if now == now.replace(hour=12, minute=0):
        print('true')
        Habit.objects.filter(needs_reset=False).update(needs_reset=True)

    for hh in h:
        if now >= hh.reset_time and hh.needs_reset:
            hh.needs_reset = False
            hh.completed = False
            print('true')
            hh.save()
    print(timezone.get_current_timezone_name())
    print(now)