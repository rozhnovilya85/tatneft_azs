import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tatneft_azs.settings')

app = Celery('tatneft_azs')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'spisok_azs': {
        'task': 'mainapp.tasks.spisok_azs',
        'schedule': (900.0)
        # 'schedule': crontab(hour=00, minute=00, day_of_month='1'),
    },
}
