from django.http import HttpResponse
from django.shortcuts import render
from .models import *
from rest_framework import generics, status
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

# Admin Portion

class Admin_regView(generics.ListCreateAPIView):
    queryset = Admin_reg.objects.all()
    serializer_class = Admin_regSerializer
    permission_classes = [AllowAny]

class AdminLoginView(generics.ListAPIView):
    queryset = Admin_reg.objects.all()
    serializer_class = AdminLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')  # Use request.data for POST requests
        password = request.data.get('password', '')

        users = Admin_reg.objects.filter(username=username, password=password)
        print(users)

        if users.exists():
            user = users.first()  # Retrieve the first user from the queryset
            serializer = self.serializer_class(user)  # Use the serializer class directly
            return Response({'message': 'Login Successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        



#Student portion 


class Student_reg(generics.ListCreateAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer
    permission_classes = [AllowAny]

class StudentLoginView(generics.ListAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = StudentLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')  # Use request.data for POST requests
        password = request.data.get('password', '')

        users = stud_reg.objects.filter(username=username, password=password)
        print(users)

        if users.exists():
            user = users.first()  # Retrieve the first user from the queryset
            serializer = self.serializer_class(user)  # Use the serializer class directly
            return Response({'message': 'Login Successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)
        


class StudentDetail(generics.RetrieveAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer


class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer


class StudentDelete(generics.DestroyAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer





                        #Course Portion Starts Here




        
class CourseCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]   

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseDelete(generics.DestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


    #Topic Start Here


class Course_Topic_Create(generics.ListCreateAPIView):
    queryset = Course_Topic.objects.all()
    serializer_class = Course_TopicSerializer
    permission_classes = [AllowAny]  


class Course_TopicDetail(generics.ListCreateAPIView):
    serializer_class = Course_TopicSerializer
    lookup_field = 'course_enrollment_id'

    def get_queryset(self):
        course_enrollment_id = self.kwargs.get('course_enrollment_id')
        queryset = Course_Topic.objects.filter(course_enrollment_id=course_enrollment_id)
        return queryset

class Course_TopicUpdate(generics.RetrieveUpdateAPIView):
    serializer_class = Course_TopicSerializer
    lookup_field = 'id'

    def get_queryset(self):
        course_enrollment_id = self.kwargs.get('id')
        queryset = Course_Topic.objects.filter(id=course_enrollment_id)
        return queryset
        
        
class CourseNameListView(APIView):
    def get(self, request, format=None):
        courses = Course.objects.all()  # Assuming Course is the model representing the course data
        serializer = CourseNameSerializer(courses, many=True)
        return Response(serializer.data)
    
class Course_TopicUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course_Topic.objects.all()
    serializer_class = Course_TopicSerializer


class Course_TopicDelete(generics.DestroyAPIView):
    queryset = Course_Topic.objects.all()
    serializer_class = Course_TopicSerializer   

class Course_Materials_Create(generics.ListCreateAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class = Course_MaterialsSerializer
    permission_classes = [AllowAny]  


class CourseMaterialsListAPIView(generics.ListAPIView):
    serializer_class = Course_MaterialsSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        return Course_Materials.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id)     
           
class MaterialsDetail(generics.RetrieveAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class = Course_MaterialsSerializer     


class MaterialUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class = Course_MaterialsSerializer
       
        #Assessment


class Assessment_Create(generics.ListCreateAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer
    permission_classes = [AllowAny]    

class AssessmentDetail(generics.RetrieveAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer


class AssessmentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer


class AssessmentDelete(generics.DestroyAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer

#Monitoring 
    
class Monitoring_Assesment(generics.ListCreateAPIView):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer
    permission_classes = [AllowAny]  

class MonitoringDetail(generics.RetrieveAPIView):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer


class MonitoringUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer


class MonitoringDelete(generics.DestroyAPIView):
    queryset = Monitoring.objects.all()
    serializer_class = MonitoringSerializer

    
class Course_purchased(generics.ListCreateAPIView):
    queryset = course_purchased.objects.all()
    serializer_class = course_purchasedSerializer
    permission_classes = [AllowAny]  

class TotalCountView(APIView):
    def get(self, request):
        student_count = stud_reg.objects.count()
        course_count = Course.objects.count()
        return Response({'student_count': student_count,'course_count':course_count})  


class CourseMaterialsCountAPIView(APIView):
    def get(self, request):
        # Get the count for each type based on course_enrollment_id and module
        counts = Course_Materials.objects.values('course_enrollment_id', 'module', 'type').annotate(total_count=models.Count('id'))
        
        # Convert queryset to list of dictionaries
        counts_list = [
            {
                'course_enrollment_id': item['course_enrollment_id'],
                'module': item['module'],
                'type': item['type'],
                'total_count': item['total_count']
            } for item in counts
        ]

        return Response(counts_list)   