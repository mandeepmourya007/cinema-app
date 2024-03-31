from __future__ import absolute_import, unicode_literals
from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cinema_project.settings')

app = Celery('cinema_project')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'update_movie_rankings': {
        'task': 'movies.tasks.update_movie_rankings',
        'schedule': timedelta(seconds=5),
    },
}
