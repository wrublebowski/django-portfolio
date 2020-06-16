from django.urls import path
from todo_app import views

app_name = 'todo_app'

urlpatterns = [
    # authoristation
    path('signup/', views.signupuser, name='signupuser'),
    path('login/', views.loginuser, name='loginuser'),
    path('logout/', views.logoutuser, name='logoutuser'),
    # todo
    path('', views.home, name='home'),
    path('current/', views.currenttodos, name='currenttodos'),
    path('create/', views.createtodo, name='createtodo'),
    path('done/', views.donetodos, name='donetodos'),
    path('todo/<int:todo_pk>', views.viewtodo, name="viewtodo"),
    path('todo/<int:todo_pk>/complete', views.completetodo, name="completetodo"),
    path('todo/<int:todo_pk>/delete', views.deletetodo, name="deletetodo"),

]
