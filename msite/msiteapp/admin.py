from django.contrib import admin

from msiteapp.models import User, Class, Student, Parent, Course, EducationReport, Marks, HomeWorks, HwAnswer


admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(EducationReport)
admin.site.register(Marks)
admin.site.register(HomeWorks)
admin.site.register(HwAnswer)