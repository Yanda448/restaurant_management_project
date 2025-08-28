import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management.settings')

app = Celery('restaurant_management')
app.config_from_object('django.conf:settings', namespace='Celery')
app.autodiscover_tasks()