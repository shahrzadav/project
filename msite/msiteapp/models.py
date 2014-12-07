from django.db import models

from django.core.files.storage import FileSystemStorage
#fs = FileSystemStorage(location='C:/Users/mina/Desktop/proj/mysite/tafrihi/statics')


class User(models.Model):
    user_id = models.CharField(max_length=16, primary_key=True)
    #username = models.CharField(max_length=20)
    password = models.CharField(max_length=10)

    job = models.CharField(max_length=10)

    def __unicode__(self):
        return self.user_id


class Parent(models.Model):
    parent_id = models.ForeignKey(User, primary_key=True)


class Classes(models.Model):
    class_id = models.CharField(max_length=15, primary_key=True)
    class_num = models.CharField(max_length=20)


class Course(models.Model):
    course_id = models.CharField(max_length=15, primary_key=True)
    course_name = models.CharField(max_length=20)
    class_id = models.ForeignKey(Classes)
    year = models.IntegerField(max_length=4)


class Teacher(models.Model):
    teacher_id = models.ForeignKey(User, primary_key=True)
    course_id = models.ForeignKey(Course)
    teacher_name = models.CharField(max_length=20)
    teacher_family = models.CharField(max_length=20)


class Student(models.Model):
    student_id = models.ForeignKey(User, primary_key=True)
    parent_id = models.ForeignKey(Parent)
    class_id = models.ForeignKey(Classes)


class Adviser(models.Model):
    adviser_id = models.ForeignKey(User, primary_key=True)


class HWQ(models.Model):
    hw_id = models.CharField(max_length=15, primary_key=True)
    course_id = models.ForeignKey(Course)
    hw_file = models.FileField()


class HWA(models.Model):
    hw_a_id = models.CharField(max_length=15, primary_key=True)
    hw_id = models.ForeignKey(HWQ)
    student_id = models.ForeignKey(Student)
    hw_a_file = models.FileField()


class Message(models.Model):
    massage_id = models.CharField(max_length=15, primary_key=True)
    topic = models.CharField(max_length=20)
    text = models.TextField()
#    sender = models.ForeignKey(User)
#    receiver = models.ForeignKey(User)
    date = models.DateTimeField()
    ############# answer_to_which = models.ForeignKey(Message)


class AdviserMessage(models.Model):
    ad_massage_id = models.CharField(max_length=15, primary_key=True)
    topic = models.CharField(max_length=20)
    text = models.TextField()