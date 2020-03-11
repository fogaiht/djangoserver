from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from core.views import PlayerViewSet


ROUTER = routers.DefaultRouter()
ROUTER.register(r'players', PlayerViewSet)

urlpatterns = [
    path('', include(ROUTER.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
]
