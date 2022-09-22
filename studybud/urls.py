
import http
import re
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('base.urls')),
    path('api/' , include('base.api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root =settings.MEDIA_ROOT ) #we're setting a url and the file path is MEDIA_URL from settings and get the file from MEDIA_ROOT