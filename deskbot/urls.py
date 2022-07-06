from . import views
from django.urls import path


urlpatterns = [
    path('deskbot', views.deskbot),
    path('answering', views.answering)
]