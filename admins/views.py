from django.shortcuts import render, redirect ,reverse
from django.http import HttpResponse
from django.views.generic import DetailView, CreateView

from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from admins.forms import RegistrationForm

# Create your views here.

@login_required()
def profile(request):
    print("User.id",request.user.id)
    url = reverse("admins.profile", args=[request.user.id])
    # return  HttpResponse("Hello, world. You're at the profile of mysite.")
    return redirect(url)


class AdminsDetailView(DetailView):
    model = User
    template_name = 'admins/admins_detail.html'


## register ???
class AdminCreateView(CreateView):
    model = User
    template_name = 'admins/create.html'
    form_class = RegistrationForm
    success_url = "/admins/login"

def index(request):
    return render(request, "admins/index.html")
