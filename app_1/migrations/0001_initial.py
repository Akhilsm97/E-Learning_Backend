# Generated by Django 4.0 on 2024-03-02 07:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Admin_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('admin_name', models.CharField(max_length=200)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Assessment_add',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assessment_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
                ('due_date', models.DateField()),
                ('total_points', models.CharField(max_length=50)),
                ('weight', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=50)),
                ('submission_method', models.CharField(choices=[('Online', 'Online'), ('offline', 'Offline')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('course_enrollment_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_name', models.CharField(max_length=50)),
                ('course_instructor', models.CharField(max_length=50)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('level', models.CharField(choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')], max_length=100)),
                ('price', models.IntegerField()),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Inactive', 'Inactive')], max_length=100)),
                ('created_at', models.DateField()),
                ('course_img', models.ImageField(upload_to='courses/')),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='stud_reg',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stud_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=200)),
                ('Address_line_1', models.CharField(max_length=200)),
                ('Address_line_2', models.CharField(max_length=200)),
                ('qualification', models.CharField(max_length=200)),
                ('percent_mark', models.DecimalField(decimal_places=2, max_digits=5)),
                ('username', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('stud_img', models.ImageField(upload_to='students/')),
                ('reg_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Monitoring',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('mark', models.CharField(max_length=50)),
                ('results', models.CharField(max_length=50)),
                ('assessment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.assessment_add')),
                ('course_enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.stud_reg')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('module', models.IntegerField(choices=[(1, 'Module 1'), (2, 'Module 2'), (3, 'Module 3'), (4, 'Module 4'), (5, 'Module 5'), (6, 'Module 6'), (7, 'Module 7'), (8, 'Module 8'), (9, 'Module 9'), (10, 'Module 10')])),
                ('topic_title', models.CharField(max_length=50)),
                ('topic_details', models.CharField(max_length=500)),
                ('course_enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course')),
            ],
        ),
        migrations.CreateModel(
            name='course_purchased',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('duration', models.IntegerField()),
                ('course_enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course')),
                ('stud_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.stud_reg')),
            ],
        ),
        migrations.CreateModel(
            name='Course_Materials',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_title', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('Thumbnail', models.ImageField(upload_to='thumbnail/')),
                ('created_at', models.DateField()),
                ('video_url', models.URLField()),
                ('course_enrollment_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course_topic')),
            ],
        ),
        migrations.AddField(
            model_name='assessment_add',
            name='course_enrollment_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course'),
        ),
        migrations.AddField(
            model_name='assessment_add',
            name='module',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_1.course_topic'),
        ),
    ]