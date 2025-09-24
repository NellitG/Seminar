from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserViewSet

router = DefaultRouter()
router.register(r'accounts', CustomUserViewSet, basename='accounts')

urlpatterns = [
    path('', include(router.urls)),
]