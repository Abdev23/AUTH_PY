
from django.shortcuts import render


def app(request):
  return render(
    request,
    'app.html',
    context = {}
  )


def home(request):
  return render(
    request,
    'main.html',
    {
      'main_templates': 'main_home.html'
    }
  )


def messages(request):
  return render(
    request,
    'main.html',
    {
      'main_templates': 'main_messages.html'
    }
  )


def posts(request):
  return render(
    request,
    'main.html',
    {
      'main_templates': 'main_posts.html'
    }
  )