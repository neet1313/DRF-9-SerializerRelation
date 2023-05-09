from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SingerViewset, SongViewset

router = DefaultRouter()
router.register('singer', SingerViewset)
router.register('song', SongViewset)

urlpatterns = [
    path('', include(router.urls)),
]
