from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import APIView

from .serializers import Postserializer
from rest_framework.viewsets import ModelViewSet 
from .models import Post

from rest_framework.permissions import IsAuthenticated

from rest_framework import filters

from .filters import PostFilter
from django_filters.rest_framework  import DjangoFilterBackend
# Create your views here.

class HelloView(APIView):
    
    def get(self,request):
        return Response({"Infor":"Learn Django-rest-framework"})

class Postview(ModelViewSet):
    serializer_class =Postserializer
    permission_classes =[IsAuthenticated]
    filter_backends =[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filter_class = PostFilter
    ordering_fields =['id','title','status']
    search_fields =['title','content']
    def get_queryset(self):
        return Post.objects.filter()
