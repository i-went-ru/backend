from django.urls import include, path
from rest_framework import routers

from .views import TourViewSet

router = routers.DefaultRouter()
router.register('', TourViewSet)

urlpatterns = [
    path('', include(router.urls))
]
