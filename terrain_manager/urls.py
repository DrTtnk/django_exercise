from django.urls import path
from . import views

urlpatterns = [
    path('get_all',         views.get_all, name='terrains-get-all'),
    path('get/<int:id>',    views.get,     name='terrains-get'),
    path('update/<int:id>', views.update,  name='terrains-update'),
    path('delete/<int:id>', views.destroy, name='terrains-destroy'),
]
