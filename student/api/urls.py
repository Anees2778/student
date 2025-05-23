from django.urls import path
from student.views import *

urlpatterns = [
    path('',HomeView.as_view(), name="userslist"),  
    path('create/',CreateStudentView.as_view(), name="create-student"),
    path('<int:pk>/',HandleStudentView.as_view(), name="handleStudent"),
    path('update/<int:pk>/',UpdateAPIView.as_view(), name="updateStudent"),
]