from django.http import HttpRequest
from django.shortcuts import redirect, render
from main.forms import UserSignupForm

# Create your views here.

def index(request: HttpRequest):
    return render(request, 'main/index.html')

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


def profile(request: HttpRequest):
    form = UserSignupForm()
    context = {
        'form': form
    }
    
    return render(request, 'main/profile.html', context)

def navbar(request: HttpRequest):
    return render(request, 'main/components/sample.html')
