from django.urls import include,path
from users import views as user_views
from django.contrib.auth import views as auth_views

appname = 'users'
urlpatterns = [
    path('success/',user_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('profile/',auth_views.LogoutView.as_view(template_name='users/profile.html'),name='profile')
]