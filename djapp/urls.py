from . import views
from django.urls import path

urlpatterns = [
    path('home/',views.home , name='home'),
    path('show/<student_id>',views.show ,name='show'),
    path('delete/<student_id>',views.delete ,name='delete'),
    path('add/',views.addStudent, name='add'),
    path('edit/<student_id>',views.editStudent ,name='edit')

]
