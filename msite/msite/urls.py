from django.conf.urls import patterns, include, url
from django.contrib import admin
from msiteapp.views import login_user, user_logout, report_st

urlpatterns = patterns('',
    #Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', login_user),
    url(r'^student/(?P<a>.+)/karname/', report_st),
    url(r'^logout/', user_logout),


)
