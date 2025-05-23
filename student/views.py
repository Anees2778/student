from django.shortcuts import render, redirect
from rest_framework.views import APIView
from student.models import Student
from student.serializers import StudentSerializer
from student.forms import *
# Create your views here.

# class SortedStudents(APIView):
#     students=


class HomeView(APIView):
    def get(self, request):
        # students=Student.objects.filter(address='l', weight__gt=50,).order_by('-testScore')
        # students=Student.objects.filter(weight__gt=67)
        students=Student.objects.all()
        return render (request,'student/home.html',{'students':students})
    
class CreateStudentView(APIView):
    def get(self, request):
        form =CreateStudentForm()
        return render(request,'student/createStudent.html',{'form':form})
    
    def post(self,request):
        form= CreateStudentForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('../')
        else:
            return render(request,'student/error.html',{'error':"Invalid details!!!!"})
    
class HandleStudentView(APIView):
    
    def get(self, request, pk):
        try:
            student = Student.objects.get(pk=pk)
            form = CreateStudentForm(instance=student)
            return render(request, 'student/studentDetail.html', {'form': form})
        except Student.DoesNotExist:
            return render(request, 'student/error.html', {'error': "Student not found"})
    
    def post(self, request, pk):
        if 'delete' in request.POST :
            try:
                student=Student.objects.get(pk=pk)
                student.delete()
                return redirect('../')
            except Student.DoesNotExist:
                return render(request,'student/error.html',{'error':"Student with the following id Doesn't exist"})
        
class UpdateAPIView(APIView):
    def get(self, request, pk):
        student=Student.objects.get(pk=pk)
        form =CreateStudentForm(instance=student)
        return render(request, 'student/update.html',{'form': form})
    
    def post(self, request, pk):
        if 'update' in request.POST :
            student=Student.objects.get(pk=pk)
            serializer=StudentSerializer(student, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return redirect('../../')
            # else:
            #     return render(request,'student/error.html',{'error':serializer.error})
            
        
        
    
    
    # def delete(self,request,pk):
    #     print("hello    Anees!!!!!!!!")