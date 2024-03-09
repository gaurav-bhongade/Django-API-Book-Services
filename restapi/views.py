from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet
from rest_framework.mixins import *
from restapi.models import Book
from restapi.serializer import BookSerialization
from rest_framework.permissions import AllowAny,IsAdminUser,BasePermission
# Create your views here.

class BookOperations(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Book.objects.all()
    serializer_class = BookSerialization

    def get_permissions(self):
        if self.action in ('retrive',):
            self.permission_classes = [IsAdminUser,]
        return super(self.__class__, self).get_permissions()

'''    
class MyOwnViewset(CreateModelMixin, UpdateModelMixin):
    pass

class BookOperations(MyOwnViewset):
    queryset = Book.objects.all()
    serializer_class = BookSerialization
'''