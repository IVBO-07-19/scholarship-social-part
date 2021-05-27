from django.contrib import admin
from django.urls import path, include

from main_app.views import *

urlpatterns = [
    path('onetime/create/', CreateOneTimeView.as_view()),
    path('onetime/<int:pk>/', OneTimeView.as_view()),
    path('onetime/list/all/', ListOneTimeView.as_view()),
    path('onetime/list/own/', ListOwnOneTimeView.as_view()),
    path('onetime/rate/<int:pk>/', RateOneTimeView.as_view()),
    path('onetime/byapp/<int:pk>/', OnetimeByAppIDView.as_view()),

    path('systematic/create/', CreateSystematicView.as_view()),
    path('systematic/<int:pk>/', SystematicView.as_view()),
    path('systematic/list/', ListSystematicView.as_view()),
    path('systematic/list/own/', ListOwnSystematicView.as_view()),
    path('systematic/rate/<int:pk>/', RateSystematicView.as_view()),
    path('systematic/byapp/<int:pk>/', SystematicByAppIDView.as_view()),

    path('volunteer/create/', CreateVolunteerView.as_view()),
    path('volunteer/<int:pk>/', VolunteerView.as_view()),
    path('volunteer/list/', ListVolunteerView.as_view()),
    path('volunteer/list/own/', ListOwnVolunteerView.as_view()),
    path('volunteer/rate/<int:pk>/', RateVolunteerView.as_view()),
    path('volunteer/byapp/<int:pk>/', VolunteerByAppIDView.as_view()),

    path('information/create/', CreateInformationSupportView.as_view()),
    path('information/<int:pk>/', InformationSupportView.as_view()),
    path('information/list/', ListInformationSupportView.as_view()),
    path('information/list/own/', ListOwnInformationSupportView.as_view()),
    path('information/rate/<int:pk>/', RateInformationSupportView.as_view()),
    path('information/byapp/<int:pk>/', InformationSupportByAppIDView.as_view()),

    path('article/create/', CreateArticleView.as_view()),
    path('article/<int:pk>/', ArticleView.as_view()),
    path('article/list/', ListArticleView.as_view()),
    path('article/list/own/', ListOwnArticleView.as_view()),
    path('article/rate/<int:pk>/', RateArticleView.as_view()),
    path('article/byapp/<int:pk>/', ArticleByAppIDView.as_view()),

]
