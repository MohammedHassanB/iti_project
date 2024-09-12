from django.urls import include, path
from admins.views import  AdminCreateView, profile, AdminsDetailView,index
from django.contrib.auth.decorators import login_required
urlpatterns = [

    # path('', include('django.contrib.auth.urls')),
    path('index',index, name='admins.index'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>', login_required(AdminsDetailView.as_view()), name='admins.profile'),
    path("create", AdminCreateView.as_view(), name="register")
]