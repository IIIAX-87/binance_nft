import os

from celery import Celery


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "binance_nft.settings")

app = Celery("binance_nft")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
