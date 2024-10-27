# videoapp/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_video, name='upload_video'),
    path('result/<int:video_id>/', views.result, name='result'),
]

