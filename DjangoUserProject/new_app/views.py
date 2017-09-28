from django.shortcuts import render
from new_app.models import User

from new_app.forms import AddUser
from . import forms

# Create your views here.
def index(request):

    null_dict = {}
    return render(request, 'new_app/index.html',context = null_dict)

def users(request):

    users = User.objects.order_by('user_fn')
    users_dict = {'users': users}
    return render(request, 'new_app/users.html',context = users_dict)


def addUser(request):
    form = AddUser()
    if request.method == 'POST':
        form = AddUser(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'new_app/success.html')

    return render(request, 'new_app/adduser.html', {'form':form})
