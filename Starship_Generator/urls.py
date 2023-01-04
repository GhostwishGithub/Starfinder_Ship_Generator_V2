from django.urls import path, include
from django.contrib import admin
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/', include('authentication.urls')),
    path('api/tiers/', views.get_tiers),
    path('api/frames/', views.get_frames),
    path('api/powercores/', views.get_powercores),
    path('api/thrusters/', views.get_thrusters),
    path('api/armors/', views.get_armors),
    path('api/computers/', views.get_computers),
    path('api/crewquarters/', views.get_crewquarters),
    path('api/defensivecountermeasures/', views.get_defensivecountermeasures),
    path('api/driftengines/', views.get_driftengines),
    path('api/expansionbays/', views.get_expansionbays),
    path('api/security/', views.get_security),
    path('api/sensors/', views.get_sensors),
    path('api/shields/', views.get_shields),
    path('api/weapons/', views.get_weapons),
    path('api/personnelweaponslongarm/', views.get_personnelweaponslongarm),
    path('api/personnelweaponsheavy/', views.get_personnelweaponsheavy),
    path('api/customselect/', views.get_customselect),
    path('api/customselectlist/', views.get_customselectlist),
]