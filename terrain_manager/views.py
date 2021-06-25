import json

from django.http import JsonResponse, HttpRequest
from django.shortcuts import redirect
from .models import Terrain, User, Sensor
from django.forms.models import model_to_dict


def get_all_terrains(request: HttpRequest):
    return JsonResponse({'terrains': [model_to_dict(t) for t in Terrain.objects.all()]})


def get_terrain(request: HttpRequest, id):
    return JsonResponse({'terrain': model_to_dict(Terrain.objects.get(id=id))})


def create_terrain(request: HttpRequest):
    terrain = Terrain.objects.create()
    json_data = json.loads(request.body)

    terrain.owner = User.objects.get(json_data['owner'])
    terrain.name = json_data['name']
    terrain.description = json_data['description']
    terrain.position = json_data['position']

    return JsonResponse({'terrain': model_to_dict(terrain)})


def update_terrain(request: HttpRequest, id):
    terrain = Terrain.objects.get(id=id)
    json_data = json.loads(request.body)

    terrain.name = json_data['name']
    terrain.description = json_data['description']
    terrain.position = json_data['position']

    return JsonResponse({'terrain': model_to_dict(terrain)})


def destroy_terrain(request: HttpRequest, id):
    Terrain.objects.get(id=id).delete()
    return redirect("/get_all")


def get_all_sensors(request: HttpRequest):
    return JsonResponse({'sensors': [model_to_dict(t) for t in Sensor.objects.all()]})


def get_sensor(request: HttpRequest, id):
    return JsonResponse({'sensor': model_to_dict(Sensor.objects.get(id=id))})


def create_sensor(request: HttpRequest):
    sensor = Sensor.objects.create()
    json_data = json.loads(request.body)

    sensor.name = Terrain.objects.get(json_data['owner'])
    sensor.terrain = json_data['terrain']
    sensor.description = json_data['description']
    sensor.position = json_data['position']

    return JsonResponse({'sensor': model_to_dict(sensor)})


def update_sensor(request: HttpRequest, id):
    sensor = Sensor.objects.get(id=id)
    json_data = json.loads(request.body)

    sensor.name = json_data['name']
    sensor.description = json_data['description']
    sensor.position = json_data['position']

    return JsonResponse({'sensor': model_to_dict(sensor)})


def destroy_sensor(request: HttpRequest, id):
    Sensor.objects.get(id=id).delete()
    return redirect("/get_all")
