from django.shortcuts import render

# Create your views here.



from waffle.mixins import WaffleFlagMixin
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework import viewsets


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField(max_length=100)


class UserViewSet(WaffleFlagMixin, viewsets.ModelViewSet):
    """
    A simple ViewSet for viewing and editing Users.
    """
    waffle_flag = "my_flag"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = []