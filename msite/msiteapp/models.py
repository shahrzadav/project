from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Class(models.Model):
    class_no = models.IntegerField(unique=True)
    grade_no = models.IntegerField()

    def __str__(self):
        return '%s' % str(self.class_no)


class Student(models.Model):
    student = models.ForeignKey(User, to_field='username', unique=True)
    class_no = models.ForeignKey(Class, to_field='class_no')

    def __str__(self):
        return '%s' % str(self.student)


class Parent(models.Model):
    parent = models.ForeignKey(User, to_field='username')
    student = models.ForeignKey(Student, to_field='student')

    def __str__(self):
        return '%s' % str(self.parent)


class Course(models.Model):
    class_no = models.ForeignKey(Class, to_field='class_no')
    teacher = models.ForeignKey(User, to_field='username')
    subject = models.CharField(max_length=10)
    year = models.IntegerField()

    def __str__(self):
        return '%s %s' % (self.subject, self.class_no)


class EducationReport(models.Model):
    report_topic = models.CharField(max_length=20)  # month of report
    report_date = models.DateField('report published')
    year = models.IntegerField()
    course_id = models.ForeignKey(Course)
    base_mark = models.IntegerField(default=20)

    def __str__(self):
        return '%s' % str(self.id)


class Marks(models.Model):
    student = models.ForeignKey(User, to_field='username')
    report = models.ForeignKey(EducationReport)
    mark_val = models.IntegerField(default=0)
    description = models.CharField(max_length=80)

    def __str__(self):
        return '%s %s' % (str(self.student), str(self.mark_val))


class HomeWorks(models.Model):
    course = models.ForeignKey(Course)
    topic = models.CharField(max_length=20)
    date = models.DateField()
    q_file = models.FileField()

    def __str__(self):
        return '%s' % (str(self.topic))


class HwAnswer(models.Model):
    homework = models.ForeignKey(HomeWorks)
    student = models.ForeignKey(Student)
    answer_file = models.FileField()
    date = models.DateField()
    mark = models.IntegerField(default=0)

    def __str__(self):
        return '%s %s' % (str(self.student), str(self.homework))


class Exam(models.Model):
    course = models.ForeignKey(Course)
    date_init = models.DateField(default=datetime.now)
    date_end = models.DateField()

    def __str__(self):
        return '%s %s' % (str(self.course), str(self.id))


class ExamQuestions(models.Model):
    exam = models.ForeignKey(Exam)
    question_no = models.IntegerField(unique=True)
    question = models.TextField()
    first_choice = models.CharField(max_length=60)
    second_choice = models.CharField(max_length=60)
    third_choice = models.CharField(max_length=60)
    forth_choice = models.CharField(max_length=60)
    answer = models.IntegerField()

    def __str__(self):
        return '%s %s' % (str(self.question_no), str(self.question))


class StudentAnswer(models.Model):
    exam = models.ForeignKey(Exam)
    student = models.ForeignKey(Student)
    answer = models.IntegerField()
    question_no = models.ForeignKey(ExamQuestions, to_field='question_no')

    def __str__(self):
        return '%s %s' % (str(self.student), str(self.answer))


class ExamResult(models.Model):
    exam = models.ForeignKey(Exam)
    student = models.ForeignKey(Student)
    mark = models.IntegerField()
    date = models.DateField(default=datetime.now)

    def __str__(self):
        return '%s %s %s' % (str(self.exam), str(self.student), str(self.mark))


class Question(models.Model):
    topic = models.CharField(max_length=20)
    student = models.ForeignKey(Student)
    year = models.IntegerField()
    month = models.IntegerField()
    day = models.IntegerField()
    question_txt = models.TextField()
    course = models.ForeignKey(Course)

    def __str__(self):
        return '%s' % str(self.question_txt)


class QuestionAnswer(models.Model):
    question = models.ForeignKey(Question)
    user = models.ForeignKey(User)
    answer_date = models.DateField(default=datetime.now)
    answer_txt = models.TextField()

    def __str__(self):
        return '%s' % str(self.answer_txt)
