
from django.urls import path

from . import views


urlpatterns = [
  path('', views.app, name = 'app'),
  path('home', views.home, name = 'main_home'),
  path('message', views.messages, name = 'main_messages'),
  path('posts', views.posts, name = 'main_posts')
]