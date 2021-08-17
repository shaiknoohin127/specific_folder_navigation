from django.urls import path
from app1.views import *
app_name="app1"
urlpatterns=[
    path('app1_noo/',app1_noo,name='app1_noo'),
]