from django.urls import path
from todolist.views import RegisterView
from todolist.views import LoginView

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]