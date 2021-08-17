from django.urls import path
from app2.views import *
app_name="app2"
urlpatterns=[
    path('app2_hin',app2_hin,name='app2_hin'),
]