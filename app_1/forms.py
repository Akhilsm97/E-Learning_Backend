from django import forms
from . models import *

class stud_regForm(forms.ModelForm):
    class Meta:
        model = stud_reg
        fields = '__all__'

class LoginForm(forms.ModelForm):
    class Meta:
        model = Login
        fields = '__all__' 

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course 
        fields = '__all__' 

class Course_TopicForm(forms.ModelForm):
    class Meta:
        model = Course_Topic 
        fields = '__all__' 
        

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment_add
        fields = '__all__' 

class MonitoringForm(forms.ModelForm):
    class Meta:
        model = Monitoring
        fields = '__all__' 
        

class course_purchasedForm(forms.ModelForm):
    class Meta:
        model = course_purchased
        fields = '__all__'         