from django.contrib import admin

from msiteapp.models import User, Class, Student, Parent, Course, EducationReport, Marks, HomeWorks, HwAnswer, Exam,\
    ExamQuestions, ExamResult, ExamStudentAnswer, Question, QuestionAnswer


admin.site.register(Class)
admin.site.register(Course)
admin.site.register(Student)
admin.site.register(Parent)
admin.site.register(EducationReport)
admin.site.register(Marks)
admin.site.register(HomeWorks)
admin.site.register(HwAnswer)
admin.site.register(Exam)
admin.site.register(ExamResult)
admin.site.register(ExamQuestions)
admin.site.register(ExamStudentAnswer)
admin.site.register(Question)
admin.site.register(QuestionAnswer)
