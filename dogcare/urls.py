"""dogcare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from authapp.views import *
from django.contrib import admin
from django.contrib.auth import views as auth_views
from authapp import views as core_views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [

    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', logout_page),
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # <--
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', register),
    url(r'^register/success/$', register_success),
    url(r'^dogprofile/$', core_views.dogprofile, name='dogprofile'),
    url(r'^profile/$', core_views.user_profile, name='profile'),
    url(r'^addDogs/$', core_views.addDogs, name='addDogs'),
    url(r'^addInfo/$', core_views.addInfo, name='addInfo'),
    url(r'^profile/(?P<pk>[0-9]+)$', core_views.UpdateProfileView.as_view(),name='profile'),
    url(r'^profileDog/(?P<pk>[0-9]+)$', core_views.UpdateDogView.as_view(),name='dogProfile'),
    url(r'^delete/(?P<pk>\d+)', core_views.dog_delete, name='dog_delete'),
    url(r'^comment/$', core_views.add_comment, name='comment'),
    url(r'^summit_comment/$', core_views.summit_comment, name='summit_comment'),
    url(r'^comment_list/$', core_views.comment_list, name='comment_list'),
    url(r'^contact/$', core_views.contact, name='contact'),
    url(r'^booking/', core_views.IndexView, name="booking"),
    url(r'^time/', core_views.getTime, name='day'),
    url(r'^submit/', core_views.submit, name='submit'),
    url(r'^receipt/(?P<data>.*)', core_views.receipt, name='receipt'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)