from django.urls import path
from .views import *

urlpatterns = [
    path('sign_up', sign_up),
    path('sign_out', sign_out),
    path('sign_in', sign_in),
    path('profile', profile),
]






