from django.urls import path
from . import views


urlpatterns = [
    path('', views.helpdesk),
    path('predict', views.predict),
    path('adminPanel/feed_data', views.feed_data, name='feed_data'),
    path('adminPanel/crud', views.crud),
    path('adminPanel/train', views.train) 
]