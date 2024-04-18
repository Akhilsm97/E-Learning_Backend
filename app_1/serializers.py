from .models import *
from rest_framework import serializers

class Admin_regSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_reg
        fields = '__all__'
class AdminLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin_login
        fields = '__all__'         

class stud_regSerializer(serializers.ModelSerializer):
    stud_img = serializers.ImageField(required=False)
    reg_date = serializers.DateField(required=False)
    class Meta:
        model = stud_reg
        fields = '__all__'

class FacultySerializer(serializers.ModelSerializer):
    faculty_img = serializers.ImageField(required=False)
    reg_date = serializers.DateField(required=False)
    class Meta:
        model = faculty_reg
        fields = '__all__'   
        
class FacultyLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = FacultyLogin
        fields = '__all__'               
        

class StudentLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Login
        fields = '__all__'  

class CourseSerializer(serializers.ModelSerializer):
    course_img   = serializers.ImageField(required=False)
    created_at = serializers.DateField(required=False)
    class Meta:
        model = Course 
        fields = '__all__' 
class CourseNameSerializer(serializers.Serializer):
    course_name = serializers.CharField()
    course_enrollment_id = serializers.IntegerField()        

class Course_TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course_Topic
        fields = '__all__' 

class Course_MaterialsSerializer(serializers.ModelSerializer):
    Thumbnail = serializers.FileField(required=False)
    created_at = serializers.DateField(required=False)
    video_url = serializers.URLField(required=False)
    pdf = serializers.FileField(required=False)

    class Meta:
        model = Course_Materials
        fields = '__all__'

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment
        fields = '__all__'           

class Assessment_addSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment_add
        fields = '__all__'    
        
        
class CartDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartData
        fields = '__all__'  

class WishListSerializer(serializers.ModelSerializer):
    class Meta:
        model = WishList
        fields = '__all__'          
        

class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = '__all__' 

class course_purchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_purchased
        fields = '__all__'                       

class completedVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = completedVideos   
        fields = '__all__'         
        
        
class FinalScoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = FinalScore   
        fields = '__all__'         
             
class NotifySerializer(serializers.ModelSerializer):
    created_at = serializers.DateField(required=False)
    class Meta:
        model = Notify
        fields = '__all__'     