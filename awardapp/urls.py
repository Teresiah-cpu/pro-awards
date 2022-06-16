# from django.conf.urls import url
from django.urls import re_path as url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.home,name = 'home'),
    url(r'^profile/user$', views.profile, name='profile'),
    url(r'^project/new$', views.new_project, name='new_project'),
    url(r'^project/(\d+)', views.review, name='review'),
    url(r'^api/profile/$', views.profileList.as_view()),
    url(r'api/profile/profile-id/(?P<pk>[0-9]+)/$',views.ProfileDescription.as_view()),
    url(r'^api/project/$', views.projectList.as_view()),
    url(r'api/project/project-id/(?P<pk>[0-9]+)/$',views.ProjectDescription.as_view()),
    url(r'^search/', views.search_project, name='search_project')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)