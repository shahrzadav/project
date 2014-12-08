from django.conf.urls import patterns, include, url
from django.contrib import admin
from msiteapp.views import login_user, user_logout, report_st, report_st_mehr, report_st_aban, report_st_azar, report_st_dey, report_st_bahman, report_st_esfand, report_st_farvardin, report_st_ordibehesht, report_st_khordad

urlpatterns = patterns('',
    #Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', login_user),
    url(r'^student/(?P<a>.+)/karname/', report_st),
    url(r'^student/(?P<a>.+)/karname mehr/', report_st_mehr),
    url(r'^logout/', user_logout),


)
