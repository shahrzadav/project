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


def home(request):
    if 'username' in request.POST and request.POST['username']:
        u = request.POST['username']
        p = request.POST['password']


        sub = True
        user_id_error = False
        password_error = False
        if u == "[]" or p == "[]":
             entrance = False

        else:
            password_error = False
            user_id_error_error = False
            entrance = True

            u1 = User.objects.filter(user_id__iexact=u)
            u11 = str(u1)    # user_id

            if u11 == "[]":
                user_id_error = True

            else:
                x = User.objects.get(user_id__iexact=u)
                if x.password != p:
                    password_error = True

                else:
                    j = x.job

                    job_list = ["Parent", "Teacher", "Student", "Adviser"]
                    if j == job_list[0]:
                            #template = loader.get_template('parent.html')
                            #context = RequestContext(request)
                            #return HttpResponse(template.render(context))
                            return HttpResponseRedirect("/parent/")

                    elif j == job_list[1]:
                            #template = loader.get_template('teacher.html')
                            #context = RequestContext(request)
                            #return HttpResponse(template.render(context))
                            return HttpResponseRedirect("/teacher/")
                            #return render_to_response("teacher.html", {'u': u})
                    elif j == job_list[2]:
                            #template = loader.get_template('student.html')
                            #context = RequestContext(request)
                            #return HttpResponse(template.render(context))
                            return HttpResponseRedirect("/student/")

                    elif j == job_list[3]:
                            #template = loader.get_template('adviser.html')
                            #context = RequestContext(request)
                            #return HttpResponse(template.render(context))
                            return HttpResponseRedirect("/adviser/")

        template = loader.get_template('index.html')
        context = RequestContext(request, {'user_id_error': user_id_error, 'password_error': password_error, 'u': u, 'p': p, 'entrance': entrance, "sub": sub, "ff": u1})
        return HttpResponse(template.render(context))
    else:
        sub = False
        template = loader.get_template('index.html')
        context = RequestContext(request, {"sub": sub})
        return HttpResponse(template.render(context))


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


def report_st(request, a):
    username = a
    st_report = []
    st_mark_val = []
    st_description = []
    st_course_id = []
    st_base_mark = []
    j = 0
    for i in Marks.objects.filter(student=username):
        st_report.append(str(i.report))
        st_mark_val.append(i.mark_val)
        st_description.append(i.description)
        y = EducationReport.objects.get(id=st_report[j])
        j += 1
        st_course_id.append(str(y.course_id))
        st_base_mark.append(str(y.base_mark))

    st_list = []

    for i in range(j):
        st_sub_list = []
        st_sub_list.append(st_course_id[i])
        st_sub_list.append(st_base_mark[i])
        st_sub_list.append(str(st_mark_val[i]))
        st_sub_list.append(st_description[i])
        st_list.append(st_sub_list)


    template = loader.get_template('stgrades.html')
    context = RequestContext(request, {"st_list": st_list, "j": j})
    return HttpResponse(template.render(context))
