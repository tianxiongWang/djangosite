from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm, SignUpForm
from django.contrib.auth.models import User
from .models import UserProfile
from blog.models import Category

# Create your views here.


def user_login(request):
    if request.method == 'GET':
        # 自动生成表单
        categories = Category.objects.all()
        login_form = LoginForm()
        context = {}
        context['form'] = login_form
        context['categories'] = categories
        return render(request, "account/login.html", context=context)
    if request.method == 'POST':
        # 用POST请求来初始化表单
        login_form = LoginForm(request.POST)
        # 判断用户输入是否合法
        if login_form.is_valid():
            # 用键值对存储了表单中的数据
            data = login_form.cleaned_data
            print(data)
            user = authenticate(
                username=data['username'], password=data['password'])
            if user:
                login(request, user)
                request.session['username'] = data['username']
                return redirect('/')
            else:
                return HttpResponse('账号或密码错误')
        else:
            return HttpResponse('登录内容有误')


def user_signup(request):
    if request.method == 'GET':
        categories = Category.objects.all()
        context = {}
        context['categories'] = categories
        return render(request, 'account/signUp.html', context=context)
    else:
        user = User.objects.create_user(username=request.POST['username'])
        userProfile = UserProfile.objects.create(user=user)
        user.set_password(request.POST['password'])
        userProfile.user = user
        userProfile.mobile = request.POST['mobile']
        userProfile.email = request.POST['email']
        userProfile.nickname = request.POST['nickname']
        userProfile.QQ = request.POST['QQ']
        user.save()
        userProfile.save()
        login(request, authenticate(
            username=user.username, password=request.POST['password']))
        request.session['username'] = user.username
        print(request.session)
        return redirect('/')
