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

        

class Assessment_addSerializer(serializers.ModelSerializer):
    class Meta:
        model = Assessment_add
        fields = '__all__'    

class MonitoringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitoring
        fields = '__all__' 

class course_purchasedSerializer(serializers.ModelSerializer):
    class Meta:
        model = course_purchased
        fields = '__all__'                       
             