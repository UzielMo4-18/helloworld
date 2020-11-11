#about/urls.py
from django.urls import path

from .views import homePageView_A

urlpatterns=[
    path('',homePageView_A,name="homeA")
]