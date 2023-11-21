from django.urls import include, path

from rest_framework import routers

from .views import ResidentViewSet

router = routers.DefaultRouter()
router.register(r'', ResidentViewSet)

urlpatterns = [
    path('', include(router.urls))
]
