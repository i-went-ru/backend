from django.urls import include, path
from rest_framework import routers
from .views import UserViewSetFull

router = routers.DefaultRouter()
router.register('', UserViewSetFull)

urlpatterns = [
    path('', include(router.urls))
]
