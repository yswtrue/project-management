from django.shortcuts import render

# Create your views here.


def sign_up(request):
    if request.method == 'GET':
        return render(request, 'project/sign_up.html')
