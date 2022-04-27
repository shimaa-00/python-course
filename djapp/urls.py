from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home , name='home'),
    path('show/<student_id>',views.show ,name='show'),
    path('delete/<student_id>',views.delete ,name='delete'),
    path('add/',views.addStudent, name='add'),
    path('edit/<student_id>',views.editStudent ,name='edit'),


    path('api-all',views.api_all_students,name='api-all'),
    path('api-one/<student_id>', views.api_one_student ,name='api-one'),
    path('api-add', views.api_add_student ,name='api-add'),
    path('api-edit/<student_id>', views.api_edit_student ,name='api-edit'),
    path('api-delete/<student_id>', views.api_delete_student ,name='api-delete'),
    path('login',views.loginToAPP , name='login'),
    path('signup',views.signupToAPP , name='signup'),
    path('signout',views.signoutFromAPP , name='signout')

]
