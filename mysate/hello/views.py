from django.shortcuts import render, HttpResponse


def get_hello(request):
  return render(request, 'hello.html',{
    'title': 'Hello',
  })