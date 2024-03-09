from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer
from restapi.models import Book

class BookSerialization(ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        #fields = ('id','name','price')
        #exclude = ('id','name','price')