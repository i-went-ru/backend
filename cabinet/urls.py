from django.urls import include, path

from rest_framework import routers

from .views import CabinetViewSet

router = routers.DefaultRouter()
router.register(r'', CabinetViewSet)

urlpatterns = [
    path('', include(router.urls))
]
