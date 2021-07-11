from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import (
    ReviewViewSet,
    CategoryViewSet,
    ItemViewSet,
    CountryViewSet,
    ItemVariantViewSet,
)

router = DefaultRouter()
router.register("item", ItemViewSet)
router.register("category", CategoryViewSet)
router.register("country", CountryViewSet)
router.register("itemvariant", ItemVariantViewSet)
router.register("review", ReviewViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
