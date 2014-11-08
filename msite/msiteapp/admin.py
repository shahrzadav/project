from django.contrib import admin

from msiteapp.models import User, Parent, Classes, Course, Teacher, Student, Adviser, HWQ, HWA, Message, AdviserMessage

admin.site.register(User)
admin.site.register(Parent)
admin.site.register(Classes)
admin.site.register(Course)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Adviser)
admin.site.register(HWQ)
admin.site.register(HWA)
admin.site.register(Message)
admin.site.register(AdviserMessage)

