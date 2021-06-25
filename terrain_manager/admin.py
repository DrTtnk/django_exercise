import threading
import traceback

from django.contrib import admin
from .models import Terrain, Sensor
import time

from .views import send_mail_recap

admin.site.register(Terrain)
admin.site.register(Sensor)


def every(delay, task):
    while True:
        time.sleep(delay)
        try:
            task()
        except Exception:
            traceback.print_exc()


threading.Thread(target=lambda: every(3600 * 6, send_mail_recap)).start()
