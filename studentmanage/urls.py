from django.urls import path
from . import views


#html file, url, view for any webpage

urlpatterns =[
    path('',views.home, name='home'),
    #path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('relations/',views.relations, name='relations'),
    path('student/',views.student, name='student'),
    path('courses/',views.courses, name='courses'),
    path('professor/',views.professor, name='professor'),
    path('register/',views.register_user, name='register'),
    path('srecord/<int:pk>',views.student_record,name='srecord'),
    path('delete_srecord/<int:pk>',views.delete_srecord,name='delete_srecord'),
    path('update_srecord/<int:pk>',views.update_srecord,name='update_srecord'),
    path('crecord/<str:pk>',views.course_record,name='crecord'),
    path('delete_crecord/<str:pk>',views.delete_crecord,name='delete_crecord'),
    path('precord/<int:pk>',views.prof_record,name='precord'),
    path('delete_precord/<int:pk>',views.delete_precord,name='delete_precord'),
    path('add_student/',views.add_student, name='add_student'),
    path('add_professor/',views.add_professor, name='add_professor'),
    path('add_course/',views.add_course, name='add_course'),
    path('update_precord/<int:pk>',views.update_precord,name='update_precord'),
    path('update_crecord/<str:pk>',views.update_crecord,name='update_crecord'),
    path('student_report/<str:rollno>',views.student_report, name="student_report")
    #path('delete_record/<int:pk>',views.delete_record,name='delete_record'),
]
