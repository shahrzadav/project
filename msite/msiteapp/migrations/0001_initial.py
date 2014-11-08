# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AdviserMessage',
            fields=[
                ('ad_massage_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('topic', models.CharField(max_length=20)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('class_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('class_num', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('course_name', models.CharField(max_length=20)),
                ('year', models.IntegerField(max_length=4)),
                ('class_id', models.ForeignKey(to='msiteapp.Classes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HWA',
            fields=[
                ('hw_a_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('hw_a_file', models.FileField(upload_to='')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='HWQ',
            fields=[
                ('hw_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('hw_file', models.FileField(upload_to='')),
                ('course_id', models.ForeignKey(to='msiteapp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('massage_id', models.CharField(primary_key=True, serialize=False, max_length=15)),
                ('topic', models.CharField(max_length=20)),
                ('text', models.TextField()),
                ('date', models.DateTimeField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.CharField(primary_key=True, serialize=False, max_length=16)),
                ('password', models.CharField(max_length=10)),
                ('job', models.CharField(max_length=10)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacher_id', models.ForeignKey(to='msiteapp.User', primary_key=True, serialize=False)),
                ('teacher_name', models.CharField(max_length=20)),
                ('teacher_family', models.CharField(max_length=20)),
                ('course_id', models.ForeignKey(to='msiteapp.Course')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('student_id', models.ForeignKey(to='msiteapp.User', primary_key=True, serialize=False)),
                ('class_id', models.ForeignKey(to='msiteapp.Classes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Parent',
            fields=[
                ('parent_id', models.ForeignKey(to='msiteapp.User', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Adviser',
            fields=[
                ('adviser_id', models.ForeignKey(to='msiteapp.User', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='student',
            name='parent_id',
            field=models.ForeignKey(to='msiteapp.Parent'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hwa',
            name='hw_id',
            field=models.ForeignKey(to='msiteapp.HWQ'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='hwa',
            name='student_id',
            field=models.ForeignKey(to='msiteapp.Student'),
            preserve_default=True,
        ),
    ]
