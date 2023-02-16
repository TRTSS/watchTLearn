import random

from django.shortcuts import render, redirect
from users.models import CustomUser
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail

# Create your views here.
def HomePage(request):
    context = {
        "pageHeader": "TLearn.Watch | Вход",
    }
    if request.method == "POST":
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            context['message'] = "Успешно!"
            context['messageType'] = "success"
            return redirect('personal')
        else:
            context['message'] = "Не удалось войти в аккаунт"
            context['messageType'] = 'danger'

    return render (request, "home.html", context)

@login_required
def PersonalPage(request):
    context = {}
    if request.method == "POST":
        if request.POST.get('logout') is not None:
            logout(request)
            context['message'] = "Logout"
            return redirect('home')
        if request.POST.get('newUserBtn') is not None:
            if CustomUser.objects.filter(email=request.POST.get('newUserEmail')).exists():
                context['message'] = "Пользователь с такой эл. почтой уже существует"
            else:
                newUser = CustomUser()
                newUser.fullname = request.POST['newUserFullname']
                newUser.email = request.POST['newUserEmail']
                p = ""
                abc = "qwertyuiopasdfghjklzxcvbnm1234567890"
                while len(abc) < 8:
                    p += random.choice(abc)
                print (p)
                context['nPassword'] = p
                send_mail(
                    'Вы зарегистрированы на TLearn.Watch',
                    f'Вы были зарегистрированы на платформе TLearn. Если вы этого не делали, проигнорируйте это сообщение. Ваш пароль: {p}',
                    'support@tlearn.ru',
                    [request.POST['newUserEmail']],
                    fail_silently=False,
                )
                n = p
                newUser.set_password(p)
                newUser.userSchool = request.user.userSchool
                newUser.save()
                context['message'] = "Пользователь создан. Пароль: " + n
    if request.user.userRole.GetPower() == 0:
        return render(request, "personalUser.html", context)
    if request.user.userRole.GetPower() == 2:
        context['users'] = CustomUser.objects.filter(userSchool=request.user.userSchool)
        return render(request, "personalAdmin.html", context)