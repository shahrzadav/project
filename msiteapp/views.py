from django.shortcuts import render
from msiteapp.models import Class, Student, Parent, Course, EducationReport, Marks, HomeWorks
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from msite.forms import ModelFormWithFileField
from msite import forms
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User
from datetime import date

################################################ login & logout ################################################


def login_user(request):
    if 'username' in request.POST and request.POST['username']:

        sub = True
        entrance = False
        user_pass_error = False

        username = request.POST['username']
        password = request.POST['password']

        if username == "[]" or password == "[]":
            entrance = False

        else:
            entrance = True

            t1 = User.objects.filter(username=username)
            if str(t1) == "[]":
                user_pass_error = True

            else:
                t2 = User.objects.get(username=str(username))
                t2 = t2.password
                if str(password) == "[]":
                    user_pass_error = True
                else:
                    user = authenticate(username=username, password=password)

                    a = User.get_username(user)
                    aa = str(a)
                    part = a[0:2]

                    if user is not None:
                        if user.is_active:
                            login(request, user)

                            if part == 'pa':
                                template = loader.get_template('parent.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance,
                                                                   "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'st':
                                template = loader.get_template('student.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance,
                                                                   "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'te':
                                template = loader.get_template('teacher.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance,
                                                                   "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'ad':
                                template = loader.get_template('adviser.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance,
                                                                   "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                        else:
                            pass
                            # Return a 'disabled account' error message
                    else:
                        pass

        template = loader.get_template('index.html')
        context = RequestContext(request, {"sub": sub, "entrance": entrance, "user_pass_error": user_pass_error})
        return HttpResponse(template.render(context))
    else:
        sub = False
        template = loader.get_template('index.html')
        context = RequestContext(request, {"sub": sub})
        return HttpResponse(template.render(context))


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/home/')

##############################################grades report for student############################################


def report_st(request, a):

    template = loader.get_template('st_grades_month.html')
    context = RequestContext(request, {"a": a})
    return HttpResponse(template.render(context))


def report_st_mehr(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "مهر":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_mehr.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_aban(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "آبان":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_aban.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_azar(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "آذر":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_azar.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_dey(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "دی":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_dey.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_bahman(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "بهمن":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_bahman.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_esfand(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "اسفند":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_esfand.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_farvardin(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "فروردین":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_farvardin.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_ordibehesht(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "اردیبهشت":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_ordibehesht.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))


def report_st_khordad(request, a):
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    st_report_topic = []
    j = 0
    for i in Marks.objects.filter(student=a):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))
        st_report_topic.append(str(y.report_topic))

    st_list_tmp = []

    for i in range(j):
        st_sub_list = [st_report_topic[i], st_course_id[i][:len(st_course_id[i]) - 3], st_base_mark[i],
                       str(st_mark_val[i]), st_description[i]]
        st_list_tmp.append(st_sub_list)

    st_list = []
    for i in range(len(st_list_tmp)):
        if st_list_tmp[i][0] == "خرداد":
            st_list.append(st_list_tmp[i])
    for i in range(len(st_list)):
        st_list[i].pop(0)

    template = loader.get_template('st_grades_khordad.html')
    context = RequestContext(request, {'xx': st_list})
    return HttpResponse(template.render(context))

#########################################moshahede va download takalif #############################################


def st_courses(request, a):
    stu_user = User.objects.get(username=a)
    stu = Student.objects.get(student=stu_user)
    class_no = stu.class_no
    courses = Course.objects.filter(class_no=class_no)

    template = loader.get_template('stu-lessons-list.html')
    context = RequestContext(request, {'a': a, 'st_course_list': courses})
    return HttpResponse(template.render(context))

###########################################vared kardane nomarat tavasote teacher #################################


def which_class(a):

    return render_to_response('tea-mainreport.html', {'a': a})


def get_form(request):
    class_number = request.GET['class_no']

    rep_month = request.GET['report_month']
    sub = request.GET['subject']
    base_mark = request.GET['max_mark']
    year = request.GET['year']
    student_un = Student.objects.order_by('class_no')

    #get id of the course that is reported
    course_obj = Course.objects.get(class_no=int(class_number), subject=sub)

    #create a education report in db for current report
    report_obj = EducationReport(course_id=course_obj,
                                 report_topic=rep_month,
                                 report_date=date.today(),
                                 base_mark=base_mark,
                                 year=year)
    report_obj.save()
    report_id = report_obj.id

    #generate a table with students of that class
    class_num = []
    students = []
    for i in range(len(student_un)):
        class_num.append(student_un[i].class_no)

        if str(student_un[i].class_no) == str(class_number):
            name = []
            user_ob = User.objects.get(username=student_un[i].student)
            name.append(user_ob.first_name)
            name.append(user_ob.last_name)
            name.append(user_ob.username)
            students.append(name)

    return render_to_response('tea-report.html',
                              {'class_number': class_number,
                               'students': students,
                               'report_id': report_id})


def set_marks(request):

    class_no1 = request.GET['class_number']
    class_no = int(class_no1[:len(class_no1)-1])
    report_id = int(request.GET['report_id'])

    report_obj = EducationReport.objects.get(id=report_id)
    students = Student.objects.filter(class_no=class_no)

    for student in students:
        mark = request.GET[str(student.student)]
        stu_un = student.student
        stu_obj = User.objects.get(username=stu_un)
        new_mark = Marks(report=report_obj, student=stu_obj, mark_val=mark)
        new_mark.save()

    return render_to_response('tea-mainreport.html')
#########################################################################shahrzad


def upload_file(request):
    if request.method == 'POST':
        form = forms.ModelFormWithFileField(request.FILES)
        if form.is_valid():
            # file is saved
            form.save()
            return HttpResponseRedirect('/success/url/')
    else:
        form = forms.ModelFormWithFileField()
    return render(request, 'upload.html', {'form': form})


def enter_hw_page(request):
    find = []

    if 'grade2' in request.POST and request.POST['grade2']:

        grade2 = request.POST['grade2']
        grade3 = request.POST['grade3']
        find_course = Course.objects.get(subject=grade2, class_no=grade3)

        for i in HomeWorks.objects.filter(course=find_course):
            find.append(str(i.topic))

        return render_to_response('tea-hw-management.html', {'name': find, 'classnumber': grade3,
                                                             'find_course': find_course})

    return render(request, 'tea-class-selection.html')


def takliftopic(request):
    #render_to_response('tea-hw-details.html')
    #classnumber = request.GET['classnumber']
    return render(request, 'tea-hw-details.html')


def taklifstudent(request, classnumber):
        find_student = []
        for i in Student.objects.filter(class_no=int(classnumber)):
            j = User.objects.get(username=i.student)
            find_student.append(str(j.first_name))

        return render_to_response('tea-hw-details.html', {'find_student': find_student, 'class_no': classnumber})

    #return render(request, 'tea-hw-management.html')


def sabtetaklif(request, find_course):
    if request.method == 'POST':
        form = forms.ModelFormWithFileField(request.POST, request.FILES)
        if form.is_valid():
            #if 'upload' in request.POST:
                #sub = True
                upload = request.POST['upload']
                m = HomeWorks(course=find_course, topic=upload, date=date.today(), q_file=form)
                # file is saved
                m.save()
                return HttpResponseRedirect('/takalif/topic/')
    else:
        form = forms.ModelFormWithFileField()

    return render(request, "tea-hw-compose.html", {form: 'form'})


def sabtetaklifejadid(request):
    return render(request, 'tea-hw-compose.html')


#def set_Hw_mark(request, class_no, find_student):
    #stu_username = []
#    for j in Student.objects.filter(class_no=int(class_no)):
#            j.append(str(Student.student))
#            for i in find_student:z
#                grade=request.GET['i']

    #if request.method == 'POST':
    #    for i in find_student:
     #       mark = int(request.GET['grade'])
      #      homeworkgrades = HwAnswer(student=i, date=date.today(), mark=mark, )
       #     homeworkgrades.save()
    #return render_to_response('tea-hw-details.html')