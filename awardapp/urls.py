from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('',views.home,name = 'home'),
    path('profile/user', views.profile, name='profile'),
    path('project/new', views.new_project, name='new_project'),
    path('project/(\d+)', views.review, name='review'),
    path('api/profile/', views.profileList.as_view()),
    path('api/profile/profile-id/(<pk>[0-9]+)/',views.ProfileDescription.as_view()),
    path('api/project/', views.projectList.as_view()),
    path('api/project/project-id/(<pk>[0-9]+)/',views.ProjectDescription.as_view()),
    path('search/', views.search_project, name='search_project')
]
# if settings.DEBUG:
#     urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)