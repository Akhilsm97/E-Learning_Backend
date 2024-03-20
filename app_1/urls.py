
from django.urls import path
from . import views
from .views import *
from django.views.decorators.csrf import  csrf_exempt

urlpatterns = [
    
    #API URLS
    path('counts/', views.TotalCountView.as_view()),
    path('Q_count/<int:course_enrollment_id>/<int:module_id>/', QuestCountListAPIView.as_view()),
    

    path('create_admin/',views.Admin_regView.as_view()),
    path('admin_login/', views.AdminLoginView.as_view()),

    path('create_stud/',views.Student_reg.as_view()),
    path('student_login/', views.StudentLoginView.as_view()),
    path('stud_details/<int:pk>/', views.StudentDetail.as_view()),
    path('stud_detail/<str:username>/', views.StudentDetails.as_view()),
    path('stud_update/<int:pk>/', views.StudentUpdateView.as_view()),
    path('stud/<int:pk>/delete/', views.StudentDelete.as_view()),
    
    #Faculty API
    
    path('create_faculty/',views.Faculty_reg.as_view()),
    path('faculty_details/<int:pk>/', views.FacultyDetail.as_view()),
    path('faculty_update/<int:pk>/', views.FacultyUpdateView.as_view()),
    path('faculty/<int:pk>/delete/', views.FacultyDelete.as_view()),

    #Course API
    path('create_course/',views.CourseCreate.as_view()),
    path('course_details/<int:pk>/', views.CourseDetail.as_view()),
    path('course_update/<int:pk>/', views.CourseUpdateView.as_view()),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view()),
    path('course-names/', CourseNameListView.as_view(), name='course-names-list'),
    path('course_materials/<int:course_enrollment_id>/<int:module_id>/', CourseMaterialsListAPIView.as_view()),
    path('material_details/<int:pk>/', views.MaterialsDetail.as_view()),
    path('material_update/<int:pk>/', views.MaterialUpdateView.as_view()),
    

    #Create Topic

    path('create_topic/',views.Course_Topic_Create.as_view()),
    path('topic_details/<int:course_enrollment_id>/', views.Course_TopicDetail.as_view()),
    path('topic_update/<int:id>/', views.Course_TopicUpdate.as_view()),
    path('topic/<int:pk>/delete/', views.Course_TopicDelete.as_view()),
    path('Course_Materials/',views.Course_Materials_Create.as_view()),
    path('course_module/<int:course_enrollment_id>/<int:module_id>/', CourseModuleListAPIView.as_view()),
    path('course-materials/count/', CourseMaterialsCountAPIView.as_view(), name='course_materials_count'),
    path('course-question/count/', CourseQuestionCountAPIView.as_view(), name='course_materials_count'),
    

    path('assessment/',views.AssessmentView.as_view()),
    path('create_assessment/',views.Assessment_Create.as_view()),
    path('Assessment_details/<int:pk>/', views.AssessmentDetail.as_view()),
    path('Assessment_update/<int:pk>/', views.AssessmentUpdateView.as_view()),
    path('Assessment/<int:pk>/delete/', views.AssessmentDelete.as_view()),
    path('assessmentQ/<int:course_enrollment_id>/', views.AssessmentQDetail.as_view()),
    path('assessmentQuestion/<int:course_enrollment_id>/', views.AssessmentQuestionDetail.as_view()),
    path('assessment_Q/<int:course_enrollment_id>/<int:module_id>/', AssessmentQuestListAPIView.as_view()),



    path('monitoring/', views.Monitoring_Assesment.as_view()),
    path('Monitoring_details/<int:pk>/', views.MonitoringDetail.as_view()),
    path('Monitoring_update/<int:pk>/', views.MonitoringUpdateView.as_view()),
    path('Monitoring/<int:pk>/delete/', views.MonitoringDelete.as_view()),
    
    path('cart/', views.CartDataView.as_view()),
    path('cart_details/<int:stud_reg>/', views.CartDetail.as_view()),
    path('C_count/<int:stud_reg>/', CartCountView.as_view()),
    path('Cart_Detail/<int:pk>/', views.CartDetailView.as_view()),
    path('C_total/<int:stud_reg>/', CartTotalView.as_view()),
    path('Cart/<int:pk>/delete/', views.CartDelete.as_view()),
    path('course_purchased/', views.Course_purchased.as_view()),
    
    path('create-checkout-session/<pk>/', csrf_exempt(CreateCheckOutSession.as_view()), name='checkout_session'),


    
    


]