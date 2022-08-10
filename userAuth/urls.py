from django.urls import path
from . import views

urlpatterns = [
    path('advanced/', views.user_login, name='signin'),
    path('logout/', views.user_logout),
]