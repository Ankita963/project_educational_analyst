from unicodedata import name
from django.contrib import admin
from django.urls import path
from . import views
from authentication import views
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
   path('', views.home,name="home"),
   path('signup', views.signup,name="signup"),
   path('signin', views.signin,name="signin"),
   path('signout', views.signout,name="signout"),
   path('uploadfunc', views.uploadfunc,name="uploadfunc"),
   path('dashboard', views.home_page_view),
   path('createprofile', views.createprofile),
   #path('createprofileedit', views.createprofileedit),
   path('qualification/',views.qualificationdetails),
   path('qualification1/',views.qualificationdetails1),
   path('qualification2/',views.qualificationdetails2),
   path('qualification3/',views.qualificationdetails3),
   path('qualification4/',views.qualificationdetails4),
   path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
   path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
   path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
   path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
   path('researchpaper/',views.research_paper),
   path('patents/',views.patents),
   path('certificate/',views.certificate),
   path('experience/',views.experience),
   path('project/',views.project),
   path('skills/',views.skills),
   path('achievements/',views.achievements),
   path('createprofileview/',views.createprofile_view),
   path('patentsview/',views.patents_view),
   path('certificateview/',views.certificate_view),
]


if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


