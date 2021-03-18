from rest_framework import serializers

from .models import *


class ApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Application
        depth = 1
        fields = '__all__'


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        depth = 1
        fields = '__all__'
