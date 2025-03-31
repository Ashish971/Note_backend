from django.urls import path
from todolist.views import RegisterView, LogoutView
from todolist.views import LoginView , TodoCreateView

urlpatterns =[
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
   path('logout/', LogoutView.as_view(), name='logout'),
    path('todos/create/', TodoCreateView.as_view(), name='todo-create'),

]