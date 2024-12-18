from .views import *
from django.urls import path,include
from rest_framework.routers import DefaultRouter
#
# router=DefaultRouter()
# router.register(r"persons",PeopleViewSet,basename="persons")
# urlpatterns=router.urls


urlpatterns=[
    # path("",include(router.urls)),
    path('person/',person),
    path("login/",login),
    path("persons/",PersonApi.as_view()),
    path('register/',RegisterApi.as_view()),
    path('logins/',LoginApi.as_view()),
]