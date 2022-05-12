from ast import Assign
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from main.forms import SubmissionForm, UserSignupForm
from main.models import Assignment, Klass, Profile, Subject
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

# Create your views here.
# ========UTITLITY FUNCTIONS

def portal_selection(request: HttpRequest):
    user = request.user
    print(user.is_authenticated)
    if not user.is_authenticated:
        return redirect('login')
    if not Profile.objects.filter(user=user).exists():
        return HttpResponse("You can not login, contact your admin")
    if user.profile.is_student():
        return redirect('student_home')
    else:
        return redirect('teacher_home')


# ==================================
def index(request: HttpRequest):
    return portal_selection(request)

@login_required
def view_assignment(request: HttpRequest, id: int):
    assignment = get_object_or_404(Assignment, pk=id)
    form = SubmissionForm()
    context = {
        'assignment':assignment,
        'form': form
    }
    return render(request, 'main/assignments/view.html', context)
    
@login_required
def subject_assignments(request: HttpRequest, id: int):
    subject = get_object_or_404(Subject ,pk=id)
    assignments = Assignment.objects.filter(id=id)
    context = {
        'subject': subject,
        'assignments': assignments
    }
    return render(request, 'main/assignments/home.html', context)

@login_required
def student_home(request: HttpRequest):
    student = request.user.profile.student
    klass = student.klass
    subjects = klass.subjects.all()

    print(subjects)

    context = {
        'klass' : student.klass.name,
        'subjects' : subjects
    }
    return render(request, 'main/student/home.html', context)
@login_required
def teacher_home(request: HttpRequest):
    return render(request, 'main/teacher/home.html')

def signup(request: HttpRequest):
    if request.method == "GET":
        form = UserSignupForm()
        context = {
            'form': form
        }
        return render(request, 'main/auth/signup.html', context)
    else:
        data = request.POST.copy()
        data['email'] = data.get('email').lower()
        username = data['email']
        form = UserSignupForm(data)
        if form.is_valid():
            # print(new_user.username)
            new_user = form.save(commit=False)
            new_user.username = username
            new_user.save()
        return redirect('index')


@login_required
def profile(request: HttpRequest):
    form = UserSignupForm()
    context = {
        'form': form
    }
    
    return render(request, 'main/profile.html', context)

def navbar(request: HttpRequest):
    return render(request, 'main/components/sample.html')
