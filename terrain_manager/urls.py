from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login_page, name='login'),

    path('terrain/get_all',         views.get_all_terrains, name='terrains-get-all'),
    path('terrain/get/<int:id>',    views.get_terrain,      name='terrains-get'),
    path('terrain/create/<int:id>', views.create_terrain,   name='terrains-create'),
    path('terrain/update/<int:id>', views.update_terrain,   name='terrains-update'),
    path('terrain/delete/<int:id>', views.destroy_terrain,  name='terrains-destroy'),

    path('sensor/get_all',         views.get_all_sensors, name='sensors-get-all'),
    path('sensor/get/<int:id>',    views.get_sensor,      name='sensors-get'),
    path('sensor/create/<int:id>', views.create_sensor,   name='sensors-create'),
    path('sensor/update/<int:id>', views.update_sensor,   name='sensors-update'),
    path('sensor/delete/<int:id>', views.destroy_sensor,  name='sensors-destroy'),
]
