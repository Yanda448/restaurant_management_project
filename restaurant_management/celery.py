import os
from celery import Celery

#Set default Django settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_management_project.settings')

app = Celery('restaurant_management_project')

#Load task settings from Django
app.config_from_object('django.conf:settings', namespace='Celery')

#Auto-discover tasks.py in all apps
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')