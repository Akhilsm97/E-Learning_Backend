from django.db import models

# Create your models here.
class Admin_reg(models.Model):
    admin_name = models.CharField(max_length = 200)
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    status = models.CharField(max_length = 200)

    def __str__(self):
        return  self.admin_name

class Admin_login(models.Model):
    username = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)

    def __str__(self):
        return  self.admin_name

class stud_reg(models.Model):
    
    Stud_name  = models.CharField(max_length = 200)
    gender_choices=[
        ('Male','Male'),
        ("Female",'Female'),
    ]
    gender  = models.CharField(choices=gender_choices, max_length = 200)
    email  = models.CharField(max_length = 200)
    phone  = models.CharField(max_length = 200)
    Address_line_1  = models.CharField(max_length = 200)
    Address_line_2  = models.CharField(max_length = 200)
    qualification = models.CharField(max_length = 200)
    percent_mark = models.DecimalField(max_digits=5, decimal_places=2)
    username  = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    stud_img=models.ImageField(upload_to='students/')
    reg_date = models.DateField()

    def __str__(self):
        return self.Stud_name
    
class Login(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)  


class Course(models.Model):
    COURSE_LEVEL_CHOICES = [
        ('Beginner', 'Beginner'),
        ('Intermediate', 'Intermediate'),
        ('Advanced', 'Advanced'),
    ]
    
    COURSE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    
    course_enrollment_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50)
    course_instructor = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    level = models.CharField(max_length=100, choices=COURSE_LEVEL_CHOICES)
    price = models.IntegerField()
    status = models.CharField(max_length=100, choices=COURSE_STATUS_CHOICES)
    created_at = models.DateField()
    course_img=models.ImageField(upload_to='courses/')

    def __str__(self):
        return self.course_name          
    

class Course_Topic(models.Model):
    TOPIC_MODULE_CHOICES = [
        (1, 'Module 1'),
        (2, 'Module 2'),
        (3, 'Module 3'),
        (4, 'Module 4'),
        (5, 'Module 5'),
        (6, 'Module 6'),
        (7, 'Module 7'),
        (8, 'Module 8'),
        (9, 'Module 9'),
        (10, 'Module 10'),

    ]
    course_enrollment_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.IntegerField(choices=TOPIC_MODULE_CHOICES)
    topic_title = models.CharField(max_length=50)
    topic_details = models.CharField(max_length=500)


    def __str__(self):
        return self.topic_title    
    
class Course_Materials(models.Model):
    
    course_enrollment_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Course_Topic, on_delete=models.CASCADE)
    video_title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    Thumbnail = models.FileField(upload_to='thumbnail/')
    created_at = models.DateField()
    video_url = models.URLField(blank=True)
    pdf = models.FileField(upload_to='pdf/', blank=True)
    
    def __str__(self):
        return self.video_title + '---> ' + str(self.course_enrollment_id)
    

class Assessment(models.Model):
    course_enrollment_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Course_Topic, on_delete=models.CASCADE)
    exam_level = models.CharField(max_length=100)
    total_question = models.IntegerField()
    total_points = models.IntegerField()
    pass_mark = models.IntegerField()
    
        




    
class Assessment_add(models.Model):
    ASSESSMENT_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    ASSESSMENT_STATUS_SUBBMISIION = [
        ('Online', 'Online'),
        ('offline', 'Offline'),
    ]
    course_enrollment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Course_Topic, on_delete = models.CASCADE)
    assessment_name = models.CharField(max_length=50)
    question  = models.CharField(max_length = 5000)
    option_1 = models.CharField(max_length=5000)
    option_2 = models.CharField(max_length=5000)
    option_3 = models.CharField(max_length=5000)
    option_4 = models.CharField(max_length=5000)
    correct_answer = models.CharField(max_length=5000)
    status = models.CharField(max_length=50, choices= ASSESSMENT_STATUS_CHOICES)
    submission_method = models.CharField(max_length=50, choices=ASSESSMENT_STATUS_SUBBMISIION)
    question_no = models.IntegerField()

    def __str__(self):
        return self.assessment_name
    
class CartData(models.Model):
    COURSE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    course_enrollment_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_reg = models.ForeignKey('stud_reg', on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.CharField(max_length=100, choices=COURSE_STATUS_CHOICES)
    created_at = models.DateField()
    course_img = models.URLField()
    username  = models.CharField(max_length = 200)
    def __str__(self) :
        return self.stud_name +' - '+ self.course_name

class WishList(models.Model):
    COURSE_STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    ]
    course_enrollment_id =  models.ForeignKey(Course, on_delete=models.CASCADE)
    stud_reg = models.ForeignKey('stud_reg', on_delete=models.CASCADE)
    stud_name = models.CharField(max_length=50)
    course_name = models.CharField(max_length=50)
    price = models.IntegerField()
    status = models.CharField(max_length=100, choices=COURSE_STATUS_CHOICES)
    created_at = models.DateField()
    course_img = models.URLField()
    wishlist_status = models.IntegerField()
    
    def __str__(self) :
        return self.stud_name +' - '+ self.course_name
        
    
    

class Monitoring(models.Model):
    stud_id = models.ForeignKey(stud_reg, on_delete=models.CASCADE)
    assessment_id = models.ForeignKey(Assessment_add, on_delete=models.CASCADE)
    course_enrollment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    description = models.CharField(max_length=50)
    mark = models.CharField(max_length=50)
    results = models.CharField(max_length=50)    

class course_purchased(models.Model):
    stud_id = models.ForeignKey(stud_reg, on_delete=models.CASCADE)
    course_enrollment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    duration = models.IntegerField()
    

    def __str__(self):
        return f"{self.stud_name} - {self.course_name}"
    
class faculty_reg(models.Model):
    
    faculty_name  = models.CharField(max_length = 200)
    gender_choices=[
        ('Male','Male'),
        ("Female",'Female'),
    ]
    gender  = models.CharField(choices=gender_choices, max_length = 200)
    email  = models.CharField(max_length = 200)
    phone  = models.CharField(max_length = 200)
    Address_line_1  = models.CharField(max_length = 200)
    Address_line_2  = models.CharField(max_length = 200)
    qualification = models.CharField(max_length = 200)
    department = models.CharField(max_length = 200)
    username  = models.CharField(max_length = 200)
    password = models.CharField(max_length = 200)
    faculty_img=models.ImageField(upload_to='faculty/')
    reg_date = models.DateField()

    def __str__(self):
        return self.faculty_name  
    
class FacultyLogin(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)      
    

class completedVideos(models.Model):
    video_id = models.ForeignKey(Course_Materials, on_delete=models.CASCADE)
    stud_id = models.ForeignKey(stud_reg, on_delete=models.CASCADE)
    course_enrollment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Course_Topic, on_delete = models.CASCADE)
    status = models.IntegerField()
    username = models.CharField(max_length = 200)

class FinalScore(models.Model):
    stud_id = models.ForeignKey(stud_reg, on_delete=models.CASCADE)
    course_enrollment_id = models.ForeignKey(Course, on_delete=models.CASCADE)
    module = models.ForeignKey(Course_Topic, on_delete = models.CASCADE)
    correct_answer = models.IntegerField()
    wrong_answer = models.IntegerField()
    unattend = models.IntegerField()
    final_score = models.IntegerField()
    status = models.IntegerField()
    username = models.CharField(max_length = 200)
    asess_date = models.DateField()
    percent = models.IntegerField()
    
    
class Notify(models.Model):
    content  = models.CharField(max_length = 1000)
    created_at = models.DateField()    
    
    