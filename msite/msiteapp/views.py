from django.shortcuts import render
from msiteapp.models import User, Parent, Classes, Course, Teacher, Student, Adviser, HWQ, HWA, Message, AdviserMessage
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.template import RequestContext, loader
from django.shortcuts import render_to_response
from django.contrib.auth import authenticate, login


#def home(request):
#    return render_to_response('index.html')

def teacher(request):
    return render_to_response('teacher.html')
#def teacher(request):
#    u = User.objects.get(name__iexact="lale")
#    return render_to_response('teacher.html', {})


def parent(request):
    return render_to_response('parent.html')


def student(request):
    return render_to_response('student.html')


def adviser(request):
    return render_to_response('adviser.html')


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


def user_login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect('/home/')
            else:
                return HttpResponse("Your  account is disabled.")
        else:
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'index.html', {})