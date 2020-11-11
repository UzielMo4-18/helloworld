#comments/urls.py
from django.urls import path

from .views import homePageView_C

urlpatterns=[
    path('',homePageView_C,name="homeC")
]