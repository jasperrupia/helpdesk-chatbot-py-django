from django.urls import path
from . import views


app_name = 'adminPanel'
urlpatterns = [
    path('dashboard', views.dashboard, name='dashboard'),
    path('feed_docs', views.feed_docs, name='feed_docs'),
    #path('test', views.test, name='test'),

    path('profile', views.profile, name='profile'),
    path('updateProfile', views.updateProfile),

    path('theme', views.theme, name='theme'),
    path('feedbacks', views.feedbacks, name='feedbacks'),
    
]
