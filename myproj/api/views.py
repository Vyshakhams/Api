from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .dataBinding import UserDataBinding
from .models import ok


class HeroViewSet(viewsets.ModelViewSet):
    # queryset = User.objects.all().order_by('id')
    serializer_class = UserDataBinding

    def get_queryset(self):
        emp = ok.objects.all()
        return emp
