from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import HttpResponse
from .models import Topic, Room, Message, Display, Profile
from .forms import DisplayForm, ProfileForm, TopicForm, RoomForm, MessageForm

# Create your views here.

def home_view(request, *args, **kwargs):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(host__username__icontains=q)
    )

    topics = Topic.objects.all()
    displays = Display.objects.all()
    # rooms = Room.objects.all()
    topics_count = topics.count()
    rooms_count = rooms.count()
    display_count = displays.count()
    context = {
        "topics": topics, "rooms": rooms,
        "displays": displays,"rooms_count":rooms_count,
        "topics_count": topics_count, "display_count": display_count
    }
    return render(request, "base/home.html", context)
    # return HttpResponse("Hello World!!!")

def topic_view(request, pk, *args, **kwargs):
    topics = Topic.objects.get(id=pk)
    context = {"topics": topics}
    return render(request, "base/topic.html", context)

def room_view(request, pk, *args, **kwargs):
    room = Room.objects.get(id=pk)
    messages = room.message_set.all()

    if request.method == "POST":
        message = Message.objects.create(
            host = request.user,
            room = room,
            body = request.POST.get("body"),
        )
        return redirect("room", pk=room.id)
    context = {"messages": messages, "room": room}
    return render(request, "base/room.html", context)

@login_required(login_url="login")
def edit_room_view(request, pk, *args, **kwargs):
    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    if request.method == "POST":
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect("room", pk=room.id)
        else:
            messsages.error(request, "An error occurred")
            return redirect("room", pk=room.id)
    context = {"form": form}
    return render(request, "base/edit_room.html", context)

@login_required(login_url="login")
def delete_room_view(request, pk, *args, **kwargs):
    room = Room.objects.get(id=pk)
    if request.method == "POST":
        room.delete()
        return redirect("home")
    context = {"obj": room}
    return render(request, "base/delete.html", context)

@login_required(login_url="login")
def create_room_view(request, *args, **kwargs):
    form = RoomForm()
    if request.method == "POST":
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "An error occurred")
    context = {"form": form}
    return render(request, "base/create_room.html", context)

@login_required(login_url="login")
def create_topic_view(request, *args, **kwargs):
    form = TopicForm()
    if request.method == "POST":
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "An error occurred")
    context = {"form": form}
    return render(request, "base/create_topic.html", context)

@login_required(login_url="login")
def blog_view(request, pk, *args, **kwargs):
    display = Display.objects.get(id=pk)
    context = {"display": display}
    return render(request, "base/blog.html", context)

@login_required(login_url="login")
def create_post_view(request, *args, **kwargs):
    form = DisplayForm()
    if request.method == "POST":
        form = DisplayForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "An error occurred")
    context = {"form": form}
    return render(request, "base/create_blog.html", context)

@login_required(login_url="login")
def edit_post_view(request, pk, *args, **kwargs):
    posts = Display.objects.get(id=pk)
    form = DisplayForm(instance=posts)
    if request.method == "POST":
        form = DisplayForm(request.POST, instance=posts)
        if form.is_valid():
            form.save()
            return redirect("home")
    if request.user != posts.host:
        return HttpResponse("You can't edit someone else's post")
    context = {"form": form}
    return render(request, "base/create_blog.html", context)

@login_required(login_url="login")
def delete_post_view(request, pk, *args, **kwargs):
    post = Display.objects.get(id=pk)
    if request.method == "POST":
        post.delete()
        return redirect("home")
    context = {"obj": post}
    return render(request, "base/delete.html", context)

def profile_view(request, pk, *args, **kwargs):
    profile = Profile.objects.get(id=pk)
    context = {"profile": profile}
    return render(request, "base/profile.html", context)

@login_required(login_url="login")
def create_profile_view(request, *args, **kwargs):
    form = ProfileForm()
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            messages.error(request, "An error occurred")
            return redirect("create-profile")
    context = {"form": form}
    return render(request, "base/create_profile.html", context)

@login_required(login_url="login")
def edit_profile_view(request, pk, *args, **kwargs):
    profile = Profile.objects.get(id=pk)
    form = ProfileForm(instance=profile)
    if request.method == "POST":
        form = ProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect("profile", pk=profile.host.id)
        else:
            message.error(request, "An error occurred")
            return redirect("profile", pk=profile.host.id)
    context = {"form": form}
    return render(request, "base/edit_profile.html", context)

def login_view(request, *args, **kwargs):
    # if request.user.is_authenticated():
    #     return redirect("home")
    page = "login"
    if request.method == "POST":
        username = request.POST["username"].lower()
        password = request.POST["password"]
        try:
            user= User.objects.get(username=username)
        except:
            messages.error(request, "Username doesn't exist")
            return redirect("login")
        user = authenticate(request, username=username, password=password)
        if user != None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Username or Password does not exist")
    context = {"page": page}
    return render(request, "base/login.html", context)

def register_view(request, *args, **kwargs):
    form  = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("create-profile")
        else:
            messages.error(request, "An error occurred")
            return redirect("register")
    context = {"form": form}
    return render(request, "base/login.html", context)

def logout_view(request, *args, **kwargs):
    logout(request)
    return redirect("home")

@login_required(login_url="login")
def delete_message_view(request, pk, *args, **kwargs):
    message = Message.objects.get(id=pk)
    if request.method == "POST":
        message.delete()
        return redirect("room", pk=message.room.id)
    context = {"obj": message}
    return render(request, "base/delete.html", context)

@login_required(login_url="login")
def edit_message_view(request, pk, *args, **kwargs):
    message = Message.objects.get(id=pk)
    form = MessageForm(instance=message)
    if request.method == "POST":
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect("room", pk=message.room.id)
        else:
            messages.error(request, "An error occurred when updating the message")
            return redirect("room", pk=message.room.id)
    context = {"form": form}
    return render(request, "base/edit_message.html", context)
