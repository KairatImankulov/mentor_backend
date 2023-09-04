from django.urls import path
from rest_framework.routers import DefaultRouter


from .api import AnnouncementViewSet, CategoryViewSet, SubCategoryViewSet


router = DefaultRouter()

router.register('category', CategoryViewSet, basename='categories')
router.register('subcategory', SubCategoryViewSet, basename='subcategories')
router.register('', AnnouncementViewSet, basename='announcements')

urlpatterns = []

urlpatterns += router.urls