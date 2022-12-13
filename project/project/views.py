from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.translation import gettext as _
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from education.serializers import *
from education.models import *


class School:
    pass


class SchoolSerializer:
    pass


class SClassSerializer:
    pass


class SClass:
    pass


class Student:
    pass


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = 'protect/index.html'

    class Index(View):
        def get(self, request):
            string = _('Hello world')

            return HttpResponse(string)

    class SchoolViewset(viewsets.ModelViewSet):
        queryset = School.objects.all()
        serializer_class = SchoolSerializer

    class SClassViewset(viewsets.ModelViewSet):
        queryset = SClass.objects.all()
        serializer_class = SClassSerializer

    class StudentViewest(viewsets.ModelViewSet):
        queryset = Student.objects.all()
        serializer_class = SClassSerializer