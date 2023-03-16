from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static 
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.index),
    path('predict', views.predict),
    path('feed_data', views.feed_data, name='feed_data'),
    path('crud', views.crud),
    path('train', views.train) 
]

if settings.DEBUG:  
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)