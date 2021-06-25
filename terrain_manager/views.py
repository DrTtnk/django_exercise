from django.http import JsonResponse
from django.shortcuts import redirect
from .models import Terrain
from django.forms.models import model_to_dict


def get_all(request):
    return JsonResponse({
        'terrains': [model_to_dict(t) for t in Terrain.objects.all()]
    })


def get(request, id):
    return JsonResponse({
        'terrain': model_to_dict(Terrain.objects.get(id=id))
    })


def update(request, id):
    terrain = Terrain.objects.get(id=id)
    terrain.name = request
    return JsonResponse({
        'terrain': model_to_dict(terrain)
    })


def destroy(request, id):
    Terrain.objects.get(id=id).delete()
    return redirect("/show")
