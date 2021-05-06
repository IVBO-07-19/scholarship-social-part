import datetime
import json

import requests
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from main_app.models import *
from main_app.serializers import *

from custom_user.permissions import *


def get_id_and_status(token):
    data = {'Authorization': token}
    r = requests.get('http://127.0.0.1:8001/api/application/last/',
                     headers=data)

    return r


class Test(APIView):
    def get(self, request):
        return Response(data=get_id_and_status(request.headers['Authorization']))


class CreateOneTimeView(APIView):
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            work = request.data['work']
            date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d').date()
            responsible = request.data['responsible']
            is_organizer = bool(request.data['is_organizer'])
            is_co_organizer = bool(request.data['is_co_organizer'])
            is_assistant = bool(request.data['is_assistant'])
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        if is_organizer + is_co_organizer + is_assistant != 1:
            return Response('fix ur participation level', status=status.HTTP_400_BAD_REQUEST)
        r = OneTimeParticipationReport.objects.create(
            central_service_id=data['id'],
            title=title,
            work=work,
            date=date
        )

        a = OneTimeParticipationApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
            is_organizer=is_organizer,
            is_co_organizer=is_co_organizer,
            is_assistant=is_assistant
        )
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OneTimeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OneTimeParticipationApp.objects.all()
    serializer_class = OneTimeParticipationSerializer
    permission_classes = [IsOwner]


class ListOneTimeView(generics.ListAPIView):
    queryset = OneTimeParticipationApp.objects.all()
    serializer_class = OneTimeParticipationSerializer
    permission_classes = [IsAdmin]


class ListOwnOneTimeView(generics.ListAPIView):
    queryset = None
    serializer_class = OneTimeParticipationSerializer

    def get(self, request):
        self.queryset = OneTimeParticipationApp.objects.filter(owner=request.user).order_by('-id')
        return super().list(request)


class RateOneTimeView(APIView):
    permission_classes = [IsAdmin]

    def put(self, request, pk):
        a = OneTimeParticipationApp.objects.get(pk=pk)
        try:
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateSystematicView(APIView):
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            work = request.data['work']
            start_date = datetime.datetime.strptime(request.data['start_date'], '%Y-%m-%d').date()
            finish_date = datetime.datetime.strptime(request.data['finish_date'], '%Y-%m-%d').date()
            responsible = request.data['responsible']
            is_organizer = request.data['is_organizer']
            is_co_organizer = request.data['is_co_organizer']
            is_assistant = request.data['is_assistant']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        if is_organizer + is_co_organizer + is_assistant != 1:
            return Response('fix ur participation level', status=status.HTTP_400_BAD_REQUEST)
        r = SystematicReport.objects.create(
            central_service_id=data['id'],
            title=title,
            work=work,
            start_date=start_date,
            finish_date=finish_date
        )

        a = SystematicApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
            is_organizer=is_organizer,
            is_co_organizer=is_co_organizer,
            is_assistant=is_assistant
        )
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SystematicView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystematicApp.objects.all()
    serializer_class = SystematicSerializer


class ListSystematicView(generics.ListAPIView):
    queryset = SystematicApp.objects.all()
    serializer_class = SystematicSerializer


class ListOwnSystematicView(generics.ListAPIView):
    queryset = None
    serializer_class = SystematicSerializer

    def get(self, request):
        self.queryset = SystematicApp.objects.filter(owner=request.user).order_by('-id')
        return super().list(request)


class RateSystematicView(APIView):
    permission_classes = [IsAdmin]

    def put(self, request, pk):
        a = SystematicApp.objects.get(pk=pk)
        try:
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = SystematicSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateVolunteerView(APIView):
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            work = request.data['work']
            date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d').date()
            responsible = request.data['responsible']
            is_leader = request.data['is_leader']
            is_organizer = request.data['is_organizer']
            is_teamleader = request.data['is_teamleader']
            is_volunteer = request.data['is_volunteer']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        if is_organizer + is_leader + is_teamleader + is_volunteer != 1:
            return Response('fix ur participation level', status=status.HTTP_400_BAD_REQUEST)
        r = VolunteerReport.objects.create(
            central_service_id=data['id'],
            title=title,
            work=work,
            date=date
        )

        a = VolunteerApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
            is_leader=is_leader,
            is_organizer=is_organizer,
            is_teamleader=is_teamleader,
            is_volunteer=is_volunteer
        )
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VolunteerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerApp.objects.all()
    serializer_class = VolunteerSerializer


class ListVolunteerView(generics.ListAPIView):
    queryset = VolunteerApp.objects.all()
    serializer_class = VolunteerSerializer


class ListOwnVolunteerView(generics.ListAPIView):
    queryset = None
    serializer_class = VolunteerSerializer

    def get(self, request):
        self.queryset = VolunteerApp.objects.filter(owner=request.user).order_by('-id')
        return super().list(request)


class RateVolunteerView(APIView):
    permission_classes = [IsAdmin]

    def put(self, request, pk):
        a = VolunteerApp.objects.get(pk=pk)
        try:
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = VolunteerSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateInformationSupportView(APIView):
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            work = request.data['work']
            start_date = datetime.datetime.strptime(request.data['start_date'], '%Y-%m-%d').date()
            finish_date = datetime.datetime.strptime(request.data['finish_date'], '%Y-%m-%d').date()
            responsible = request.data['responsible']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        r = InformationSupportReport.objects.create(
            central_service_id=data['id'],
            title=title,
            work=work,
            start_date=start_date,
            finish_date=finish_date
        )

        a = InformationSupportApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
        )
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InformationSupportView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InformationSupportApp.objects.all()
    serializer_class = InformationSupportSerializer


class ListInformationSupportView(generics.ListAPIView):
    queryset = InformationSupportApp.objects.all()
    serializer_class = InformationSupportSerializer


class ListOwnInformationSupportView(generics.ListAPIView):
    queryset = None
    serializer_class = InformationSupportSerializer

    def get(self, request):
        self.queryset = InformationSupportApp.objects.filter(owner=request.user).order_by('-id')
        return super().list(request)


class RateInformationSupportView(APIView):
    permission_classes = [IsAdmin]

    def put(self, request, pk):
        a = InformationSupportApp.objects.get(pk=pk)
        try:
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = InformationSupportSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateArticleView(APIView):
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            media_title = request.data['media_title']
            edition_level_choicer = request.data['edition_level_choicer']
            co_author_quantity = request.data['co_author_quantity']
            date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d').date()
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        r = ArticleReport.objects.create(
            central_service_id=data['id'],
            title=title,
            media_title=media_title,
            edition_level_choicer=edition_level_choicer,
            co_author_quantity=co_author_quantity,
            date=date,
        )

        a = ArticleApp.objects.create(
            owner=request.user,
            report=r,
        )
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleApp.objects.all()
    serializer_class = ArticleSerializer


class ListArticleView(generics.ListAPIView):
    queryset = ArticleApp.objects.all()
    serializer_class = ArticleSerializer


class ListOwnArticleView(generics.ListAPIView):
    queryset = None
    serializer_class = ArticleSerializer

    def get(self, request):
        self.queryset = ArticleApp.objects.filter(owner=request.user).order_by('-id')
        return super().list(request)


class RateArticleView(APIView):
    permission_classes = [IsAdmin]

    def put(self, request, pk):
        a = ArticleApp.objects.get(pk=pk)
        try:
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = ArticleSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
