from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response

from main_app.models import *
from main_app.serializers import *


class CreateOneTimeView(APIView):
    def post(self, request):
        try:
            r = OneTimeParticipationReport.objects.create(
                title=request.data['title'],
                work=request.data['work'],
                date=request.data['date']
            )

            a = OneTimeParticipationApp.objects.create(
                responsible=request.data['responsible'],
                report=r,
                is_organizer=request.data['is_organizer'],
                is_co_organizer=request.data['is_co_organizer'],
                is_assistant=request.data['is_assistant']
            )
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class OneTimeView(generics.RetrieveUpdateDestroyAPIView):
    queryset = OneTimeParticipationApp.objects.all()
    serializer_class = OneTimeParticipationSerializer


class ListOneTimeView(generics.ListAPIView):
    queryset = OneTimeParticipationApp.objects.all()
    serializer_class = OneTimeParticipationSerializer


class CreateSystematicView(APIView):
    def post(self, request):
        try:
            r = SystematicReport.objects.create(
                title=request.data['title'],
                work=request.data['work'],
                start_date=request.data['start_date'],
                finish_date=request.data['finish_date']
            )

            a = SystematicApp.objects.create(
                responsible=request.data['responsible'],
                report=r,
                is_organizer=request.data['is_organizer'],
                is_co_organizer=request.data['is_co_organizer'],
                is_assistant=request.data['is_assistant']
            )
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class SystematicView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SystematicApp.objects.all()
    serializer_class = SystematicSerializer


class ListSystematicView(generics.ListAPIView):
    queryset = SystematicApp.objects.all()
    serializer_class = SystematicSerializer


class CreateVolunteerView(APIView):
    def post(self, request):
        try:
            r = VolunteerReport.objects.create(
                title=request.data['title'],
                work=request.data['work'],
                date=request.data['date']
            )

            a = VolunteerApp.objects.create(
                responsible=request.data['responsible'],
                report=r,
                is_leader=request.data['is_leader'],
                is_organizer=request.data['is_organizer'],
                is_teamleader=request.data['is_teamleader'],
                is_volunteer=request.data['is_volunteer']
            )
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class VolunteerView(generics.RetrieveUpdateDestroyAPIView):
    queryset = VolunteerApp.objects.all()
    serializer_class = VolunteerSerializer


class ListVolunteerView(generics.ListAPIView):
    queryset = VolunteerApp.objects.all()
    serializer_class = VolunteerSerializer


class CreateInformationSupportView(APIView):
    def post(self, request):
        try:
            r = InformationSupportReport.objects.create(
                title=request.data['title'],
                work=request.data['work'],
                start_date=request.data['start_date'],
                finish_date=request.data['finish_date']
            )

            a = InformationSupportApp.objects.create(
                responsible=request.data['responsible'],
                report=r,
                scores=request.data['scores']
            )
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class InformationSupportView(generics.RetrieveUpdateDestroyAPIView):
    queryset = InformationSupportApp.objects.all()
    serializer_class = InformationSupportSerializer


class ListInformationSupportView(generics.ListAPIView):
    queryset = InformationSupportApp.objects.all()
    serializer_class = InformationSupportSerializer


class CreateArticleView(APIView):
    def post(self, request):
        try:
            r = ArticleReport.objects.create(
                title=request.data['title'],
                media_title=request.data['media_title'],
                edition_level_choicer=request.data['edition_level_choicer'],
                co_author_quantity=request.data['co_author_quantity'],
                date=request.data['date'],
            )

            a = InformationSupportApp.objects.create(
                report=r,
                scores=request.data['scores']
            )
        except KeyError:
            return Response('send full info', status=status.HTTP_400_BAD_REQUEST)
        serializer = OneTimeParticipationSerializer(r, context={'request': request})
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ArticleView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ArticleApp.objects.all()
    serializer_class = ArticleSerializer


class ListArticleView(generics.ListAPIView):
    queryset = ArticleApp.objects.all()
    serializer_class = ArticleSerializer

#
# class CreateView(APIView):
#     def create_onetime(self, request):
#         try:
#             r = OneTimeParticipationReport.objects.create(title=request.data['title'],
#                                                           work=request.data['work'],
#                                                           date=request.data['date'])
#
#             a = OneTimeParticipationApp.objects.create(responsible=request.data['responsible'],
#                                                        report=r,
#                                                        is_assistant=request.data['is_assistant'],
#                                                        is_co_organizer=request.data['is_co_organizer'],
#                                                        is_organizer=request.data['is_organizer'])
#         except KeyError:
#             return None
#         except ValueError:
#             return None
#         return OneTimeParticipationSerializer(a, context={'request': request})
#
#     def create_system(self, request):
#         try:
#             r = SystematicReport.objects.create(title=request.data['title'],
#                                                 work=request.data['work'],
#                                                 start_date=request.data['start_date'],
#                                                 final_date=request.data['final_date'])
#
#             a = SystematicApp.objects.create(responsible=request.data['responsible'],
#                                              report=r,
#                                              is_assistant=request.data['is_assistant'],
#                                              is_co_organizer=request.data['is_co_organizer'],
#                                              is_organizer=request.data['is_organizer'])
#         except KeyError:
#             return None
#         except ValueError:
#             return None
#         return SystematicSerializer(a, context={'request': request})
#
#     def create_volunteer(self, request):
#         try:
#             r = VolunteerReport.objects.create(title=request.data['title'],
#                                                work=request.data['work'],
#                                                date=request.data['date'])
#
#             a = VolunteerApp.objects.create(responsible=request.data['responsible'],
#                                             report=r,
#                                             is_leader=request.data['is_leader'],
#                                             is_teamleader=request.data['is_teamleader'],
#                                             is_volunteer=request.data['is_volunteer'],
#                                             is_organizer=request.data['is_organizer'])
#         except KeyError:
#             return None
#         except ValueError:
#             return None
#         return VolunteerSerializer(a, context={'request': request})
#
#     def create_info(self, request):
#         try:
#             r = InformationSupportReport.objects.create(title=request.data['title'],
#                                                         work=request.data['work'],
#                                                         start_date=request.data['start_date'],
#                                                         final_date=request.data['final_date'])
#
#             a = InformationSupportApp.objects.create(responsible=request.data['responsible'],
#                                                      report=r)
#         except KeyError:
#             return None
#         return InformationSupportSerializer(a, context={'request': request})
#
#     def create_article(self, request):
#         try:
#             r = ArticleReport.objects.create(title=request.data['title'],
#                                              media_title=request.data['media_title'],
#                                              edition_level_choicer=request.data['edition_level'],
#                                              co_author_quantity=request.data['co_author_quantity'],
#                                              date=request.data['date'])
#
#             a = ArticleApp.objects.create(responsible=request.data['responsible'],
#                                           report=r)
#         except KeyError:
#             return None
#         return ArticleSerializer(a, context={'request': request})
#
#     def post(self, request, category):
#         d = {'onetime': self.create_onetime,
#              'systematic': self.create_system,
#              'volunteer': self.create_volunteer,
#              'info': self.create_info,
#              'article': self.create_article}
#         obj = d.get(category)(request)
#         if obj is None:
#             return Response('Something wrong with arguments', status=status.HTTP_400_BAD_REQUEST)
#         return Response(obj, status=status.HTTP_201_CREATED)
#
#
# class ReadListView(APIView):
#     def get(self, request, category):
#         d = {'onetime': OneTimeParticipationApp,
#              'systematic': SystematicApp,
#              'volunteer': VolunteerApp,
#              'info': InformationSupportApp,
#              'article': ArticleApp}
#         d.get(category)().objects.all()
