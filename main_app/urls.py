from django.contrib import admin
from django.urls import path, include

from main_app.views import *

urlpatterns = [
    path('create/<str:category>/', CreateView.as_view()),

]
