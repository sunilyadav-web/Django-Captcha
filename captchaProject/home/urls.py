from django.urls import path
from .views import *

urlpatterns = [
    path('',test,name='home'),
    path('submit',submit,name='submit')
]

