from django.shortcuts import render

# Create your views here.
def get_library(request):
    return render(request, 'library.html',{
        'title': 'Антуан де Сент-Экзюпери — «Маленький принц».',
    })