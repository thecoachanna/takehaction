from django.shortcuts import render
from .models import User

def index(request):
    users = User.objects.count()
    context = {'users': users}
    return render(request, 'index.html', context=context)
