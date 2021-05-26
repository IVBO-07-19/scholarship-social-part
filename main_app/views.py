import datetime
import json

import requests
from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from main_app.serializers import *

from custom_user.permissions import *


def get_id_and_status(token):
    data = {'Authorization': token}
    r = requests.get('https://secure-gorge-99048.herokuapp.com/api/application/last/',
                     headers=data)

    return r


class CreateOneTimeView(APIView):
    '''
    DELETE
    '''

    class body1(serializers.Serializer):
        title = serializers.CharField()
        work = serializers.CharField()
        responsible = serializers.CharField()
        is_organizer = serializers.BooleanField()
        is_co_organizer = serializers.BooleanField()
        is_assistant = serializers.BooleanField()
        date = serializers.DateField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body1(),
                         responses={
                             '201': OneTimeParticipationSerializer(),
                             '400': 'ur application is closed',
                             '400': 'create application in central service',
                             '400': 'send full info',
                             '400': 'change date to correct',
                             '400': 'fix ur participation level',
                             '400': 'create application in central service'
                         })
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_400_BAD_REQUEST)
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


class OneTimeView(generics.RetrieveAPIView):
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

    '''
    DELETE
    '''

    class body6(serializers.Serializer):
        scores = serializers.IntegerField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body6(),
                         responses={
                             '201': OneTimeParticipationSerializer(),
                             '400': 'send full info',
                             '400': 'wrong address'
                         })
    def put(self, request, pk):
        try:
            a = OneTimeParticipationApp.objects.get(pk=pk)
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except OneTimeParticipationApp.DoesNotExist:
            return Response('wrong address', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = OneTimeParticipationSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateSystematicView(APIView):
    '''
    DELETE
    '''

    class body2(serializers.Serializer):
        title = serializers.CharField()
        work = serializers.CharField()
        responsible = serializers.CharField()
        is_organizer = serializers.BooleanField()
        is_co_organizer = serializers.BooleanField()
        is_assistant = serializers.BooleanField()
        start_date = serializers.DateField()
        final_date = serializers.DateField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body2(),
                         responses={
                             '201': SystematicSerializer(),
                             '200': 'ur application is closed',
                             '400': 'create application in central service',
                             '400': 'send full info',
                             '400': 'change date to correct',
                             '400': 'fix ur participation level',
                             '400': 'create application in central service'
                         })
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
            final_date = datetime.datetime.strptime(request.data['final_date'], '%Y-%m-%d').date()
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
        r = SystematicReport.objects.create(
            central_service_id=data['id'],
            title=title,
            work=work,
            start_date=start_date,
            final_date=final_date
        )

        a = SystematicApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
            is_organizer=is_organizer,
            is_co_organizer=is_co_organizer,
            is_assistant=is_assistant
        )
        serializer = SystematicSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SystematicView(generics.RetrieveAPIView):
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

    '''
    DELETE
    '''

    class body7(serializers.Serializer):
        scores = serializers.IntegerField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body7(),
                         responses={
                             '201': SystematicSerializer(),
                             '400': 'send full info',
                             '400': 'swrong address'
                         })
    def put(self, request, pk):
        try:
            a = SystematicApp.objects.get(pk=pk)
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except SystematicApp.DoesNotExist:
            return Response('wrong address', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = SystematicSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateVolunteerView(APIView):
    '''
    DELETE
    '''

    class body3(serializers.Serializer):
        title = serializers.CharField()
        work = serializers.CharField()
        responsible = serializers.CharField()
        is_organizer = serializers.BooleanField()
        is_leader = serializers.BooleanField()
        is_volunteer = serializers.BooleanField()
        is_teamleader = serializers.BooleanField()
        date = serializers.DateField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body3(),
                         responses={
                             '201': VolunteerSerializer(),
                             '200': 'ur application is closed',
                             '400': 'create application in central service',
                             '400': 'send full info',
                             '400': 'change date to correct',
                             '400': 'fix ur participation level',
                             '400': 'create application in central service'
                         })
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
            is_leader = bool(request.data['is_leader'])
            is_organizer = bool(request.data['is_organizer'])
            is_teamleader = bool(request.data['is_teamleader'])
            is_volunteer = bool(request.data['is_volunteer'])
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
        serializer = VolunteerSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VolunteerView(generics.RetrieveAPIView):
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

    '''
    DELETE
    '''

    class body8(serializers.Serializer):
        scores = serializers.IntegerField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body8(),
                         responses={
                             '201': VolunteerSerializer(),
                             '400': 'send full info',
                             '400': 'wrong address'
                         })
    def put(self, request, pk):
        try:
            a = VolunteerApp.objects.get(pk=pk)
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except VolunteerApp.DoesNotExist:
            return Response('wrong address', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = VolunteerSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateInformationSupportView(APIView):
    '''
    DELETE
    '''

    class body4(serializers.Serializer):
        title = serializers.CharField()
        work = serializers.CharField()
        responsible = serializers.CharField()
        start_date = serializers.DateField()
        final_date = serializers.DateField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body4(),
                         responses={
                             '201': InformationSupportSerializer(),
                             '200': 'ur application is closed',
                             '400': 'create application in central service',
                             '400': 'send full info',
                             '400': 'change date to correct',
                             '400': 'fix ur participation level',
                             '400': 'create application in central service'
                         })
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
            final_date = datetime.datetime.strptime(request.data['final_date'], '%Y-%m-%d').date()
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
            final_date=final_date
        )

        a = InformationSupportApp.objects.create(
            owner=request.user,
            responsible=responsible,
            report=r,
        )
        serializer = InformationSupportSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InformationSupportView(generics.RetrieveAPIView):
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

    '''
    DELETE
    '''

    class body9(serializers.Serializer):
        scores = serializers.IntegerField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body9(),
                         responses={
                             '201': InformationSupportSerializer(),
                             '400': 'send full info',
                             '400': 'wrong address'
                         })
    def put(self, request, pk):
        try:
            a = InformationSupportApp.objects.get(pk=pk)
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except InformationSupportApp.DoesNotExist:
            return Response('wrong address', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = InformationSupportSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateArticleView(APIView):
    '''
    DELETE
    '''

    class body5(serializers.Serializer):
        title = serializers.CharField()
        meida_title = serializers.CharField()
        edition_level_choicer = serializers.CharField()
        co_author_quantity = serializers.IntegerField()
        date = serializers.DateField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body5(),
                         responses={
                             '201': ArticleSerializer(),
                             '200': 'ur application is closed',
                             '400': 'create application in central service',
                             '400': 'send full info',
                             '400': 'change date to correct',
                             '400': 'fix ur participation level',
                             '400': 'create application in central service'
                         })
    def post(self, request):
        response = get_id_and_status(request.headers['Authorization'])
        if response.status_code != 200:
            return Response('create application in central service', status=status.HTTP_400_BAD_REQUEST)
        data = json.loads(response.text)
        d = {
            'municipal': ArticleReport.MUNICIPAL,
            'university': ArticleReport.UNIVERSITY
        }
        if not data['status']:
            return Response('ur application is closed', status=status.HTTP_200_OK)
        try:
            title = request.data['title']
            media_title = request.data['media_title']
            edition_level_choicer = d.get(request.data['edition_level_choicer'])
            co_author_quantity = request.data['co_author_quantity']
            date = datetime.datetime.strptime(request.data['date'], '%Y-%m-%d').date()
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ValueError:
            return Response('change date to correct', status=status.HTTP_400_BAD_REQUEST)
        if edition_level_choicer is None:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
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
        serializer = ArticleSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleView(generics.RetrieveAPIView):
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

    '''
    DELETE
    '''

    class body10(serializers.Serializer):
        scores = serializers.IntegerField()

    @swagger_auto_schema(operation_description='creates new application',
                         request_body=body10(),
                         responses={
                             '201': ArticleSerializer(),
                             '400': 'send full info',
                             '400': 'wrong address'
                         })
    def put(self, request, pk):
        try:
            a = ArticleApp.objects.get(pk=pk)
            a.scores = request.data['scores']
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        except ArticleApp.DoesNotExist:
            return Response('wrong address', status=status.HTTP_400_BAD_REQUEST)
        a.save()
        serializer = ArticleSerializer(a, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)
