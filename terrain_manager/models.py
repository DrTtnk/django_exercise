from django.db import models as m
from django.contrib.auth.models import User


class Terrain(m.Model):
    name = m.CharField(max_length=200)
    description = m.TextField(null=True, blank=True)
    position = m.CharField(max_length=200)
    owner = m.ForeignKey(User, on_delete=m.CASCADE)


class Sensor(m.Model):
    name = m.CharField(max_length=200, null=True, blank=True)
    position = m.CharField(max_length=200)
    terrain = m.ForeignKey(Terrain, on_delete=m.CASCADE)


def send_mail(user: User):
    user.terrain_set()
