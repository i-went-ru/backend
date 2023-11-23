from django.urls import include, path
from rest_framework import routers

from .views import MapPhotoViewSet

router = routers.DefaultRouter()
router.register(r'', MapPhotoViewSet)

urlpatterns = [
    path('', include(router.urls))
]
