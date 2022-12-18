from django.urls import include,path
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.forms import LoginForm

appname = 'users'
urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=LoginForm),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
]