from django.conf.urls import patterns, include, url
from django.contrib import admin
from msiteapp.views import login_user, user_logout, report_st, report_st_mehr, report_st_aban, report_st_azar, report_st_dey, report_st_bahman, report_st_esfand, report_st_farvardin, report_st_ordibehesht, report_st_khordad, st_courses
from msiteapp.views import which_class, get_form, set_marks, upload_file
from msiteapp.views import enter_hw_page, taklifstudent, sabtetaklif, takliftopic, sabtetaklifejadid


urlpatterns = patterns('',
    #Examples:
    # url(r'^$', 'mysite2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^home/', login_user),
    url(r'^student/(?P<a>.+)/karname/', report_st),
    url(r'^student/(?P<a>.+)/karname mehr/', report_st_mehr),
    url(r'^student/(?P<a>.+)/karname aban/', report_st_aban),
    url(r'^student/(?P<a>.+)/karname azar/', report_st_azar),
    url(r'^student/(?P<a>.+)/karname dey/', report_st_dey),
    url(r'^student/(?P<a>.+)/karname bahman/', report_st_bahman),
    url(r'^student/(?P<a>.+)/karname esfand/', report_st_esfand),
    url(r'^student/(?P<a>.+)/karname farvardin/', report_st_farvardin),
    url(r'^student/(?P<a>.+)/karname ordibehesht/', report_st_ordibehesht),
    url(r'^student/(?P<a>.+)/karname khordad/', report_st_khordad),

    url(r'^logout/', user_logout),


    url(r'^student/(?P<a>.+)/courses/', st_courses),


    url(r'^teacher/(?P<a>.+)/gozaresh/', which_class),
    url(r'^teacher/showlist/', get_form),
    url(r'^teacher/setmarks/', set_marks),


    url(r'^student_hw/', upload_file),
    url(r'^upload/', upload_file),
    url(r'^taklif/',enter_hw_page),
    #url(r'^takalif/topic/',takliftopic),
    url(r'^(?P<classnumber>.+)/takalif/aaaalaki/',taklifstudent),
    #url(r'^takalif/students/(?P<find_course>.+)',taklifstudent),
    url(r'^(?P<find_course>.+)/takalif/sabtetaklif', sabtetaklif),
    #url(r'^takalif/sabtetaklifejadid', sabtetaklifejadid)

)
