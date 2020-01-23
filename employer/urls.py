from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.index,name = 'index'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^applicant/(\d+)',views.applicant,name ='applicant'),
    url(r'^new/applicant$', views.new_applicant, name='new-applicant'),
    url(r'^profile/',views.profile, name='profile'),
    url(r'^profile_update/',views.profile_update,name='update')
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)