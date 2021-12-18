from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_view, name="home"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register_view, name="register"),

    path("blog/<str:pk>/", views.blog_view, name="blog"),
    path("room/<str:pk>/", views.room_view, name="room"),
    path("topic/<str:pk>/", views.topic_view, name="topic"),
    path("profile/<str:pk>/", views.profile_view, name="profile"),

    path("create_post", views.create_post_view, name="create-post"),
    path("create_room", views.create_room_view, name="create-room"),
    path("create_topic", views.create_topic_view, name="create-topic"),

    path("edit_post/<str:pk>/", views.edit_post_view, name="edit-post"),
    path("edit_room/<str:pk>/", views.edit_room_view, name="edit-room"),
    path("edit_profile/<str:pk>/", views.edit_profile_view, name="edit-profile"),
    path("edit_message/<str:pk>/", views.edit_message_view, name="edit-message"),

    path("delete_post/<str:pk>/", views.delete_post_view, name="delete-post"),
    path("delete_message/<str:pk>/", views.delete_message_view, name="delete-message"),
]
