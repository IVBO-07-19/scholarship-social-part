from rest_framework import serializers

from .models import *

from custom_user.serializers import CustomUserSerializer


class OneTimeParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = OneTimeParticipationApp
        depth = 1
        fields = '__all__'

    owner = CustomUserSerializer()


class SystematicSerializer(serializers.ModelSerializer):
    class Meta:
        model = SystematicApp
        depth = 1
        fields = '__all__'

    owner = CustomUserSerializer()


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = VolunteerApp
        depth = 1
        fields = '__all__'

    owner = CustomUserSerializer()


class InformationSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationSupportApp
        depth = 1
        fields = '__all__'

    owner = CustomUserSerializer()


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArticleApp
        depth = 1
        fields = '__all__'

    owner = CustomUserSerializer()
