from django.urls import path
from .views import RegisterView,LoginView,UserView,LogoutView

urlpatterns = [
    path('sign-up', RegisterView.as_view()),
    path('sign-in', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),

]
