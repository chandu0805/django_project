from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_gmail, name='send_gmailpage'),
]
