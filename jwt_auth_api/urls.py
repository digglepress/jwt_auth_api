from django.urls import path
from authentication.views import RegisterAPI, LoginAPI, UserAPI

urlpatterns = [
    path('login', LoginAPI.as_view()),
    path('register', RegisterAPI.as_view()),
    path('', UserAPI.as_view()),
]
