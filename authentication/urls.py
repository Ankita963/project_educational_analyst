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
   path('createprofileview/',views.createprofile_view),
   path('createprofile_edit/',views.createprofile_edit),
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
   path('researchpaperview/',views.researchpaper_view),
   path('researchpaperedit/',views.researchpaper_edit),
   path('patents/',views.patents),
   path('patentsview/',views.patents_view),
   path('patentsedit/',views.patents_edit),
   path('certificate/',views.certificate),
   path('certificateview/',views.certificate_view),
   path('certificateedit/',views.certificate_edit),
   path('experience/',views.experience),
   path('experienceview/',views.experience_view),
   path('experienceedit/',views.experience_edit), 
   path('project/',views.project),
   path('projectview/',views.project_view),
   path('projectedit/',views.project_edit),
   path('skills/',views.skills),
   path('skillview/',views.skill_view),
   path('skilledit/',views.skill_edit),
   path('achievements/',views.achievements),
   path('achievementsview/',views.achievements_view),
   path('achievementsedit/',views.achievements_edit),
   path('viewall/',views.viewall),
   path('resumeformat/',views.resumeformat),
   path('<int:user_id>/',views.resume),
   path('<int:user_id>/',views.resume1),
   

]


if settings.DEBUG:
  urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


