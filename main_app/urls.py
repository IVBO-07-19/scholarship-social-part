from django.contrib import admin
from django.urls import path, include

from main_app.views import *


urlpatterns = [
    path('onetime/create/', CreateOneTimeView.as_view()),
    path('onetime/<int:pk>/', OneTimeView.as_view()),
    path('onetime/list/', ListOneTimeView.as_view()),

    path('systematic/create/', CreateSystematicView.as_view()),
    path('systematic/<int:pk>/', SystematicView.as_view()),
    path('systematic/list/', ListSystematicView.as_view()),

    path('volunteer/create/', CreateVolunteerView.as_view()),
    path('volunteer/<int:pk>/', VolunteerView.as_view()),
    path('volunteer/list/', ListVolunteerView.as_view()),

    path('information/create/', CreateInformationSupportView.as_view()),
    path('information/<int:pk>/', InformationSupportView.as_view()),
    path('information/list/', ListInformationSupportView.as_view()),

    path('article/create/', CreateArticleView.as_view()),
    path('article/<int:pk>/', ArticleView.as_view()),
    path('article/list/', ListArticleView.as_view()),

]
