import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habits.settings')
app = Celery('habits')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks(['main'])

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')


app.conf.beat_schedule = {
    'reset-daily-habits':{
        'task': 'main.tasks.reset_daily_habits',
        'schedule': crontab(minute='*/1'),
    },
    'reset-time':{
        'task': 'main.tasks.reset_time',
        'schedule': crontab(hour=12,minute=2),
    },
}