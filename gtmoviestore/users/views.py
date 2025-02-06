from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm
from django.contrib.auth import login as auth_login, authenticate, logout as auth_logout
from .forms import CustomUserCreationForm, CustomErrorList
from django.contrib.auth.decorators import login_required
def signup(request):
    template_data = {}
    template_data['title'] = 'Sign Up'
    if request.method == 'GET':
        template_data['form'] = CustomUserCreationForm()
        return render(request, 'users/signup.html',
            {'template_data': template_data})
    elif request.method == 'POST':
        form = CustomUserCreationForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save()
            return redirect('users.login')
        else:
            template_data['form'] = form
            return render(request, 'users/signup.html',
                {'template_data': template_data})

def login(request):
    template_data = {}
    template_data['title'] = 'Login'
    if request.method == 'GET':
        return render(request, 'users/login.html',
        {'template_data': template_data})
    elif request.method == 'POST':
        user = authenticate(
        request,
        username = request.POST['username'],
        password = request.POST['password']
        )
        if user is None:
            template_data['error'] =\
            'The username or password is incorrect.'
            return render(request, 'users/login.html',
            {'template_data': template_data})
        else:
            auth_login(request, user)
            return redirect('home.index')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('home.index')


def reset_password(request):
    template_data = {}
    template_data['title'] = 'Reset Password'
    if request.method == 'GET':
        template_data['form'] = PasswordResetForm()
        return render(request, 'users/reset_password.html',
                      {'template_data':template_data})
    elif request.method == 'POST':
        form = PasswordResetForm(request.POST, error_class=CustomErrorList)
        if form.is_valid():
            form.save(request=request)
            return redirect('users.reset_password_done')
        
def reset_password_done(request):
    return render(request, 'users/reset_password_done.html')

@login_required
def orders(request):
    template_data={}
    template_data['title']= 'Orders'
    template_data['orders'] = request.user.order_set.all()
    return render(request, 'users/orders.html', {'template_data':template_data})