from django.shortcuts import render
from django_security.models import Employee
from django_security.serializer import EmoloyeeSerializetion
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
# Create your views here.

class EmployeeListOfOperations(ModelViewSet):
    permission_classes = (AllowAny,)
    queryset = Employee.objects.all()
    serializer_class = EmoloyeeSerializetion