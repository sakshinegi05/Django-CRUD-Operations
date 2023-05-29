from django.urls import path
from . import views

app_name = 'home'
 
urlpatterns = [
    path('', views.welcome, name='welcome'),
    path('index/', views.index, name='index'), 
    path('stu/', views.studentinfo),
    path('add/', views.index),
    path('stu/<int:_id>/delete/',views.delrec, name="delete_student"),
    path('update/home/stu/<int:_id_>', views.update, name='update_student'),
   
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout')
]
