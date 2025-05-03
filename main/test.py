from datetime import datetime, timedelta
from models import Habit

for habit in Habit.objects.all():
    print(habit.time)
print(datetime.now())