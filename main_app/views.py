from django.shortcuts import render
from rest_framework import generics

from main_app.models import *
from main_app.serializers import *


class ApplicationListView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer


class ReportListView(generics.ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class ReportDetailView(generics.RetrieveAPIView):
    serializer_class = ReportSerializer
    queryset = Report


class ApplicationDetailView(generics.RetrieveAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()


class ReportCreateView(generics.CreateAPIView):
    serializer_class = ReportSerializer
    queryset = Report.objects.all()


class ApplicationCreateView(generics.CreateAPIView):
    serializer_class = ApplicationSerializer
    queryset = Application.objects.all()
