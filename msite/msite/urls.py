from django.conf.urls import patterns, include, url
from django.contrib import admin
from msiteapp.views import home, teacher, student, parent, adviser #user_login# login

urlpatterns = patterns('',
    #Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', home),
    url(r'^teacher/(?P<u>.+)/', teacher),
    url(r'^student/', student),
    url(r'^parent/', parent),
    url(r'^adviser/', adviser),



    #url(r'^login/', login),

)
