from django.contrib.auth import views as auth_views
from django.urls import path

from mainapp.views import *

urlpatterns = [
    path("", LoginView.as_view(), name="Login"),
    path("create_user/", Create_user.as_view(), name="create_user"),
    path("registration/", RegistrationView.as_view(), name="registration"),
    path("client/", ClientView.as_view()),
    path("project/", ChartsView.as_view(), name="projects"),
    path("adwords/", adwords),
    path("adwords/callback", adwords_callback),
    path('apis/', ApisViews.as_view()),
    path('logout/', auth_views.LogoutView.as_view(next_page="Login"), name='myapp_logout'),
    path('facebook_login/', ApisViews.as_view())
]
