from django.contrib import admin
from django.urls import path, include

from main_app.views import *

urlpatterns = [
    path('report/list/',ApplicationListView.as_view() ),
    path('application/list/', ReportListView.as_view()),
    path('report/<int:pk>/', ReportDetailView.as_view()),
    path('application/<int:pk>/', ApplicationDetailView.as_view()),
    path('application/create/', ReportCreateView.as_view()),
    path('report/create/', ApplicationCreateView.as_view()),
]
