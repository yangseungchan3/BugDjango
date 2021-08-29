from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from .models import UserInfo, Photo
from .models import Board


def index(request):
    return render(request, 'index.html')


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        username = request.POST.get('username')
        userid = request.POST.get('email')
        userpw = request.POST.get('password')  # POST로 보내지는 것중 name이 userpw인 것을 가져오는것
        repw = request.POST.get('password_confirm')

        if userpw == repw:
            User = UserInfo.objects.create(username=username, userid=userid, userpw=userpw)
            User.save()
        return redirect('login')


def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    elif request.method == "POST":
        id = request.POST.get('email')
        pw = request.POST.get('password')
        User = UserInfo.objects.all()

        print(User)
        for user in User:
            if id == user.userid and pw == user.userpw:
                username = user.username
                print("username : " + username)

                return HttpResponse("<script>alert('login success')</script>")


def board(request):
    if request.method == "GET":
        return render(request, 'board.html')
    elif request.method == "POST":
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        image = request.FILES.getlist('images')
        print(title)
        print(contents)
        print(image)
        # print(Board.objects.all())
        board = Board.objects.create(title=title, contents=contents)
        board.save()
        for image in image:
            photo = Photo.objects.create(title=title, image=image)
            photo.save()

        return render(request, 'board.html')
