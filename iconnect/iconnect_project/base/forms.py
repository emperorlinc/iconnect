from django import forms
from .models import Display, Profile, Topic, Room, Message

class DisplayForm(forms.ModelForm):
    class Meta:
        model = Display
        fields = [
            "title",
            "blog",
        ]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = "__all__"
        exclude = ["host"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ["name",]


class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = [
            "topic",
            "name",
            "description",
        ]

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ["body"]
