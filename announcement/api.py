from rest_framework.views import APIView, View
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import (
    RetrieveAPIView, 
    UpdateAPIView, 
    DestroyAPIView, 
    CreateAPIView, 
    RetrieveUpdateDestroyAPIView
)

from rest_framework.views import Response
from .models import Announcement, Category, SubCategory
from .serializers import (
    AnnouncementListSerializer, 
    AnnouncementCreatListSerializer, 
    AnnouncementRetrieveListSerializer,
    AnnouncementSerializer,
    CategorySerializer,
    SubcategorySerializer,
)


class MentorView(APIView):
    def get(self, request, *args, **kwargs):
        ads = Announcement.objects.all()
        ads_json = AnnouncementListSerializer(ads, many=True)
        return Response(ads_json.data, status=200)
    
    def post(self, request):
        data = request.data
        serializer = AnnouncementCreatListSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
       

# class AnnouncementRetrieveView(RetrieveAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementUpdateView(UpdateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementDeleteView(DestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class AnnouncementCreateView(CreateAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


# class RetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
#     queryset = Announcement.objects.all()
#     serializer_class = AnnouncementSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SubCategoryViewSet(ModelViewSet):
    queryset = SubCategory.objects.all()
    serializer_class = SubcategorySerializer


class AnnouncementViewSet(ModelViewSet):
    queryset = Announcement.objects.all()
    serializer_class = AnnouncementSerializer

