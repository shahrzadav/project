from django.shortcuts import render
from msiteapp.models import User, Class, Student, Parent, Course, EducationReport, Marks
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.contrib.auth.models import User

################################################ login & logout #############################################################


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
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance, "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'st':
                                template = loader.get_template('student.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance, "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'te':
                                template = loader.get_template('teacher.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance, "user_pass_error": user_pass_error})
                                return HttpResponse(template.render(context))
                            elif part == 'ad':
                                template = loader.get_template('adviser.html')
                                context = RequestContext(request, {"sub": sub, "a": a, "entrance": entrance, "user_pass_error": user_pass_error})
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

##############################################grades report for student#####################################################


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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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
        st_sub_list = []
        st_sub_list.append(st_report_topic[i])
        st_sub_list.append(st_course_id[i][:len(st_course_id[i])-3])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
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


def st_courses(request, a):
    template = loader.get_template('stu-lessons.html')
    context = RequestContext(request, {'a': a})
    return HttpResponse(template.render(context))

