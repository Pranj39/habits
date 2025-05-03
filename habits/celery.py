import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'habits.settings')
app = Celery('habits')

app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks(['main'])

app.conf.enable_utc = True
app.conf.timezone   = settings.TIME_ZONE

app.conf.beat_schedule = {
    'reset-habits-every-minute': {
        'task': 'main.tasks.reset_habits_by_time',
        'schedule': crontab(minute='*'),
    },
}