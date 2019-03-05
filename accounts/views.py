from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST': #post 방식으로 전송이 됐다면
        if request.POST['password1'] == request.POST['password2']:
            user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
            auth.login(request, user)
            return redirect('home')
    return render(request, 'signup.html')

def login(request):
    if request.method == 'POST': #post 방식으로 전송이 됐다면
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username = username, password = password)
        #authenticate는 등록된 회원이 맞는지 확인해주는 메소드
        if user is not None: #이미 존재하는 회원이라면 
            auth.login(request, user) #로그인
            return redirect('home')
        else: #아니라면 에러창 출력
            return render(request, 'login.html', {'error' : 'username or password is incorrect'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST' :
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')

