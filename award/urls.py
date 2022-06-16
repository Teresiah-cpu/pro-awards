from django.contrib import admin
from django.contrib.auth import views 
from rest_framework.authtoken.views import obtain_auth_token

from django.urls import path, include
# from django.conf.urls import url,include
from django.contrib import admin
from django.urls import re_path as url

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'',include('awardapp.urls')),
    url('accounts/', include('registration.backends.simple.urls')),
    url('accounts/', include('django.contrib.auth.urls')),
    url(r'^api-token-auth/', obtain_auth_token)
    
]