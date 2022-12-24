from django.urls import include,path
from ..foodwebsite import settings
from users import views as user_views
from django.contrib.auth import views as auth_views
from users.forms import LoginForm

appname = 'users'
urlpatterns = [
    path('register/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html',authentication_form=LoginForm),name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
]