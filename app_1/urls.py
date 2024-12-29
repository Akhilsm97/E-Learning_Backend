
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
     path('faculty_login/', views.FacultyLoginView.as_view()),
    path('faculty_details/<int:pk>/', views.FacultyDetail.as_view()),
    path('faculty_detail/<str:username>/', views.FacultyDetails.as_view()),
    path('faculty_assign/<str:course_instructor>/', views.FacultyAssignDetails.as_view()),
    
    path('faculty_update/<int:pk>/', views.FacultyUpdateView.as_view()),
    path('faculty/<int:pk>/delete/', views.FacultyDelete.as_view()),

    #Course API
    path('create_course/',views.CourseCreate.as_view()),
    path('course_details/<int:pk>/', views.CourseDetail.as_view()),
    path('course_per/<str:course_enrollment_id>/', views.Course_PerDetails.as_view()),
    path('course_update/<int:pk>/', views.CourseUpdateView.as_view()),
    path('course/<int:pk>/delete/', views.CourseDelete.as_view()),
    path('course-names/', CourseNameListView.as_view(), name='course-names-list'),
    path('course_materials/<int:course_enrollment_id>/<int:module_id>/', CourseMaterialsListAPIView.as_view()),
    path('course_mat_video/<int:course_enrollment_id>/<int:module_id>/<int:id>/', CourseMaterialsVideoListAPIView.as_view()),

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
    path('course_material/<int:pk>/delete/', views.MaterialDelete.as_view()),
    

    path('assessment/',views.AssessmentView.as_view()),
    path('create_assessment/',views.Assessment_Create.as_view()),
    path('Assessment_details/<int:pk>/', views.AssessmentDetail.as_view()),
    path('Assessment_update/<int:pk>/', views.AssessmentUpdateView.as_view()),
    path('Assessment/<int:pk>/delete/', views.AssessmentDelete.as_view()),
    path('assessmentQ/<int:course_enrollment_id>/', views.AssessmentQDetail.as_view()),
    path('assessmentQuestion/<int:course_enrollment_id>/', views.AssessmentQuestionDetail.as_view()),
    path('assessment_Q/<int:course_enrollment_id>/<int:module_id>/', AssessmentQuestListAPIView.as_view()),
    path('assessment_wise/<int:course_enrollment_id>/<int:module_id>/<int:question_no>/', AssessmentQuestWiseAPIView.as_view()),
    



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
    path('course_purchased/<int:stud_reg>/', views.PurchasedCourseView.as_view()),
    path('Purchase_count/<int:stud_reg>/', PurchasedCountView.as_view()),
    
    path('create-checkout-session/<pk>/', csrf_exempt(CreateCheckOutSession.as_view()), name='checkout_session'),
    
    path('create_wishList/',views.WishList_reg.as_view()),
    path('wishList/<int:pk>/', views.WishListView.as_view()),
    path('wishlist_details/<int:stud_reg>/', views.WishListDetail.as_view()),
    path('wishList_update/<int:pk>/', views.WishListUpdateView.as_view()),
    path('wishList/<int:pk>/delete/', views.WishListDelete.as_view()),
    
    path('WatchedDetail/<int:stud_id>/<int:course_enrollment_id>/<int:module>/<int:video_id>/', WatchedDetail.as_view()),
    
    path('create_completedVideos/',views.completedVedios_Create.as_view()),
    
    path('final_score/',views.FinalScore_Create.as_view()),
    path('found/<int:course_enrollment_id>/<int:module_id>/<str:username>/', AssessmentFound.as_view()),
    path('each_score/<int:course_enrollment_id>/<int:module_id>/<int:stud_id>/', EachResultListAPIView.as_view()),
    path('topic_each/<int:course_enrollment_id>/<int:module>/', Course_TopicEachDetail.as_view()),
    path('each_assessment/<int:course_enrollment_id>/<int:module_id>/', EachAssessmentListAPIView.as_view()),
    path('purchase_found/<int:stud_reg>/<str:username>/', PurchaseFound.as_view()),
    
    path('faculty_stud/<int:course_enrollment_id>/', views.FacultyAssignStudDetail.as_view()),
    path('Faculty_Stud_count/<int:course_enrollment_id>/', FacultyAssignStudCount.as_view()),
    
    path('score_details/<int:course_enrollment_id>/<int:stud_id>/', views.ScoreDetails.as_view()),
    
    path('totalVideo_count/<int:course_enrollment_id>/', TotalVideoCount.as_view()),
    path('totalWatch/<int:stud_id>/<int:course_enrollment_id>/', TotalWatchedDetail.as_view()),
    path('totalWatchModule/<int:stud_id>/<int:course_enrollment_id>/<int:module>/', TotalWatchedModuleDetail.as_view()),
    
    path('create_notify/',views.NotifyCreate.as_view()),
    
    
    
    
    

    
    


]