from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from rest_framework import generics, status
from .serializers import *
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.db.models import Sum
import stripe
from django.conf import settings
from datetime import datetime
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
    
class StudentDetails(generics.RetrieveAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer
    lookup_field = 'username'  # Specify the lookup field

    def get_queryset(self):
        name = self.kwargs.get('username')
        return self.queryset.filter(username__icontains=name)


class StudentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer


class StudentDelete(generics.DestroyAPIView):
    queryset = stud_reg.objects.all()
    serializer_class = stud_regSerializer



    #Faculty 
    
class Faculty_reg(generics.ListCreateAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultySerializer
    permission_classes = [AllowAny]    

class FacultyDetail(generics.RetrieveAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultySerializer


class FacultyUpdateView(generics.RetrieveUpdateAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultySerializer


class FacultyDelete(generics.DestroyAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultySerializer
    
    
class FacultyLoginView(generics.ListAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultyLoginSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', '')  # Use request.data for POST requests
        password = request.data.get('password', '')

        users = faculty_reg.objects.filter(username=username, password=password)
        print(users)

        if users.exists():
            user = users.first()  # Retrieve the first user from the queryset
            serializer = self.serializer_class(user)  # Use the serializer class directly
            return Response({'message': 'Login Successful', 'data': serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Invalid username or password'}, status=status.HTTP_400_BAD_REQUEST)

                        #Course Portion Starts Here




        
class CourseCreate(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]   

class CourseDetail(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    
class Course_PerDetails(generics.ListAPIView):
    serializer_class = CourseSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs.get('course_enrollment_id')
        queryset = Course.objects.filter(course_enrollment_id=course_enrollment_id)
        return queryset    


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
    
class CourseModuleListAPIView(generics.ListAPIView):
    serializer_class = Course_TopicSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        return Course_Topic.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id)  
    
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
    
class CourseMaterialsVideoListAPIView(generics.ListAPIView):
    serializer_class = Course_MaterialsSerializer

    def get_queryset(self):
        id = self.kwargs['id']
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        return Course_Materials.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id, id=id)       
    
           
class MaterialsDetail(generics.RetrieveAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class = Course_MaterialsSerializer     


class MaterialUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class = Course_MaterialsSerializer
    

class MaterialDelete(generics.DestroyAPIView):
    queryset = Course_Materials.objects.all()
    serializer_class =Course_MaterialsSerializer
       
        #Assessment


class Assessment_Create(generics.ListCreateAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer
    permission_classes = [AllowAny]    

class AssessmentDetail(generics.RetrieveAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer
    
    
class AssessmentQDetail(generics.ListCreateAPIView):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        return Assessment.objects.filter(course_enrollment_id=course_enrollment_id) 
    
class AssessmentQuestionDetail(generics.ListCreateAPIView):
    serializer_class = Assessment_addSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        return Assessment_add.objects.filter(course_enrollment_id=course_enrollment_id)     
    
class AssessmentQuestListAPIView(generics.ListAPIView):
    serializer_class = Assessment_addSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        return Assessment_add.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id)          

class AssessmentQuestWiseAPIView(generics.ListAPIView):
    serializer_class = Assessment_addSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        id = self.kwargs['question_no']
        return Assessment_add.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id, question_no=id)   

class AssessmentUpdateView(generics.RetrieveUpdateAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer


class AssessmentDelete(generics.DestroyAPIView):
    queryset = Assessment_add.objects.all()
    serializer_class = Assessment_addSerializer


class AssessmentView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [AllowAny]

class AssessmentQView(generics.ListCreateAPIView):
    queryset = Assessment.objects.all()
    serializer_class = AssessmentSerializer
    permission_classes = [AllowAny]    
    
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
    
    
    # ------------------------------------------------------------Counts------------------------------------------------------------------

class TotalCountView(APIView):
    def get(self, request):
        student_count = stud_reg.objects.count()
        course_count = Course.objects.count()
        faculty_count = faculty_reg.objects.count()
        return Response({'student_count': student_count,'course_count':course_count,'faculty_count':faculty_count})  


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
    
    
class QuestCountListAPIView(generics.GenericAPIView):
    serializer_class = Assessment_addSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        
        question_count = Assessment_add.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id).count()
        
        return Response({'Q_count': question_count})    
    
    
class CourseQuestionCountAPIView(APIView):
    def get(self, request):
        # Get the count for each type based on course_enrollment_id and module
        counts = Assessment_add.objects.values('course_enrollment_id', 'module').annotate(total_count=models.Count('id'))
        
        # Convert queryset to list of dictionaries
        counts_list = [
            {
                'course_enrollment_id': item['course_enrollment_id'],
                'module': item['module'],
                'total_count': item['total_count']
            } for item in counts
        ]

        return Response(counts_list)   
    
    
class CartDataView(generics.ListCreateAPIView):
    queryset = CartData.objects.all()
    serializer_class = CartDataSerializer
    permission_classes = [AllowAny]     
    
class CartDetail(generics.RetrieveAPIView):
    queryset = CartData.objects.all()
    serializer_class = CartDataSerializer 

class CartDetailView(generics.RetrieveAPIView):
    queryset = CartData.objects.all()
    serializer_class = CartDataSerializer   
    
class CartDetail(generics.ListCreateAPIView):
    serializer_class = CartDataSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 'Inactive'
        return CartData.objects.filter(stud_reg=course_enrollment_id, status=status)      
    
    

class CartCountView(generics.GenericAPIView):
    serializer_class = CartDataSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 'Inactive'

        cart_count = CartData.objects.filter(stud_reg=course_enrollment_id,status =status).count()
        
        return Response({'C_count': cart_count})  
    
    
class PurchasedCourseView(generics.ListCreateAPIView):
    serializer_class = CartDataSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 'Active'
        return CartData.objects.filter(stud_reg=course_enrollment_id, status=status)   
    
class PurchasedCountView(generics.GenericAPIView):
    serializer_class = CartDataSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 'Active'

        cart_count = CartData.objects.filter(stud_reg=course_enrollment_id,status =status).count()
        
        return Response({'purchase_count': cart_count})     
    
class CartTotalView(generics.GenericAPIView):
    serializer_class = CartDataSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 'Inactive'

        cart_pieces = CartData.objects.filter(stud_reg=course_enrollment_id,status = status).aggregate(total_pieces=Sum('price'))
        total_pieces = cart_pieces['total_pieces'] if cart_pieces['total_pieces'] else 0
        
        return Response({'total_pieces': total_pieces})    
    
class CartDelete(generics.DestroyAPIView):
    queryset = CartData.objects.all()
    serializer_class = CartDataSerializer    
    
API_URL = "http/locahost:8000"
stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckOutSession(APIView):
    def post(self, request, *args, **kwargs):
        prod_id = self.kwargs["pk"]  # Accessing pk from kwargs
        current_date = datetime.now().date()
        try:
            product = CartData.objects.get(id=prod_id)
            print('PRODUCT DETAILS',product)
            product.status = 'Active'
            product.created_at = current_date
            product.save()
            total_price = CartData.objects.filter(id=prod_id).aggregate(total_price=Sum('price'))['total_price']
            checkout_session = stripe.checkout.Session.create(
    line_items=[
        {
            'price_data': {
                'currency': 'INR',
                'unit_amount': int(total_price) * 100,
                'product_data': {
                    'name': 'Your Product Name',
                    'description': 'Student Name: ' + product.stud_name +    '\n Course Name: ' + product.course_name,
                    'images': [  product.course_img
                                ]
                }
            },
            'quantity': 1,
        },
    ],
    metadata={
        "product_id": product.id,
    },
    mode='payment',
    success_url=settings.SITE_URL + 'success' + '/' + product.username,
    cancel_url=settings.SITE_URL + '?canceled=true',
)
            return redirect(checkout_session.url)
        except Exception as e:
            return Response({'msg': 'something went wrong while creating stripe session', 'error': str(e)}, status=500)



class WishList_reg(generics.ListCreateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    permission_classes = [AllowAny]    

class WishListView(generics.RetrieveAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    
class WishListDetail(generics.ListCreateAPIView):
    serializer_class = WishListSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['stud_reg']
        status = 0
        return WishList.objects.filter(stud_reg=course_enrollment_id,wishlist_status=status)         


class WishListUpdateView(generics.RetrieveUpdateAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer


class WishListDelete(generics.DestroyAPIView):
    queryset = WishList.objects.all()
    serializer_class = WishListSerializer
    

class completedVedios_Create(generics.ListCreateAPIView):
    queryset = completedVideos.objects.all()
    serializer_class = completedVideosSerializer
    permission_classes = [AllowAny]  
    
    
class WatchedDetail(generics.ListCreateAPIView):
    serializer_class = completedVideosSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module = self.kwargs['module']
        stud_id = self.kwargs['stud_id']
        video_id =self.kwargs['video_id']
        status = 1
        return completedVideos.objects.filter(course_enrollment_id=course_enrollment_id,module=module, stud_id=stud_id,video_id=video_id, status=status)     
    
class FinalScore_Create(generics.ListCreateAPIView):
    queryset = FinalScore.objects.all()
    serializer_class = FinalScoreSerializer
    permission_classes = [AllowAny]   
    
class AssessmentFound(generics.GenericAPIView):
    serializer_class = FinalScoreSerializer  # Set the serializer class

    def get(self, request, *args, **kwargs):
        # Retrieve parameters from URL kwargs
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module = self.kwargs['module_id']
        username = self.kwargs['username']
        status = 1  # Assuming status is always 1

        # Filter FinalScore objects based on parameters
        queryset = FinalScore.objects.filter(course_enrollment_id=course_enrollment_id,module=module,username=username,status=status).exists()
        return Response({'assess_found': queryset})
    
    
class EachResultListAPIView(generics.ListAPIView):
    serializer_class = FinalScoreSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        stud_id = self.kwargs['stud_id']
        return FinalScore.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id, stud_id=stud_id)       
    
       


    

class EachAssessmentListAPIView(generics.ListAPIView):
    serializer_class = AssessmentSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module_id']
        return Assessment.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id)          

class Course_TopicEachDetail(generics.ListAPIView):
    serializer_class = Course_TopicSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        module_id = self.kwargs['module']
        return Course_Topic.objects.filter(course_enrollment_id=course_enrollment_id, module=module_id)     
    
    
class PurchaseFound(generics.GenericAPIView):
    serializer_class = CartDataSerializer  # Set the serializer class

    def get(self, request, *args, **kwargs):
        # Retrieve parameters from URL kwargs
        stud_id = self.kwargs['stud_reg']
        username = self.kwargs['username']
        status = 'Active' # Assuming status is always 1

        # Filter FinalScore objects based on parameters
        queryset = CartData.objects.filter(stud_reg= stud_id,username=username,status=status).exists()
        return Response({'purchase_found': queryset})   
    
    
class FacultyDetails(generics.RetrieveAPIView):
    queryset = faculty_reg.objects.all()
    serializer_class = FacultySerializer
    lookup_field = 'username'  # Specify the lookup field

    def get_queryset(self):
        name = self.kwargs.get('username')
        return self.queryset.filter(username__icontains=name)  
    

class FacultyAssignDetails(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'course_instructor'  # Specify the lookup field

    def get_queryset(self):
        name = self.kwargs.get('course_instructor')
        return self.queryset.filter(course_instructor__icontains=name)    
    

class FacultyAssignStudDetail(generics.ListAPIView):
    serializer_class = CartDataSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        Status = 'Active'
        return CartData.objects.filter(course_enrollment_id=course_enrollment_id, status=Status)            
    
class FacultyAssignStudCount(generics.ListAPIView):
    serializer_class = CartDataSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        Status = 'Active'
        c_count= CartData.objects.filter(course_enrollment_id=course_enrollment_id, status=Status).count()   
        return Response({'C_count': c_count})
    
    
class FacultyAssignStudCount(generics.GenericAPIView):
    serializer_class = CartDataSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        status = 'Active'

        cart_count = CartData.objects.filter(course_enrollment_id=course_enrollment_id,status =status).count()
        
        return Response({'purchase_count': cart_count})     
    
    
class ScoreDetails(generics.ListAPIView):
    serializer_class = FinalScoreSerializer

    def get_queryset(self):
        course_enrollment_id = self.kwargs.get('course_enrollment_id')
        stud_id = self.kwargs.get('stud_id')
        queryset = FinalScore.objects.filter(course_enrollment_id=course_enrollment_id,stud_id=stud_id)
        return queryset 
    
    
class TotalVideoCount(generics.GenericAPIView):
    serializer_class = Course_MaterialsSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        

        total_count = Course_Materials.objects.filter(course_enrollment_id=course_enrollment_id).count()
        
        return Response({'total': total_count}) 
    
    
class TotalWatchedDetail(generics.GenericAPIView):
    serializer_class = completedVideosSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        stud_id = self.kwargs['stud_id']
        status = 1
        video_count = completedVideos.objects.filter(course_enrollment_id=course_enrollment_id, stud_id=stud_id, status=status).count()  
        return Response({'watch_total': video_count}) 
    
    
class TotalWatchedModuleDetail(generics.GenericAPIView):
    serializer_class = completedVideosSerializer

    def get(self, request, *args, **kwargs):
        course_enrollment_id = self.kwargs['course_enrollment_id']
        stud_id = self.kwargs['stud_id']
        module = self.kwargs['module']
        status = 1
        video_count = completedVideos.objects.filter(course_enrollment_id=course_enrollment_id, stud_id=stud_id,module=module, status=status).count()  
        return Response({'watch_total': video_count})         
    
class NotifyCreate(generics.ListCreateAPIView):
    queryset = Notify.objects.all()
    serializer_class = NotifySerializer
    permission_classes = [AllowAny]                

        
                 