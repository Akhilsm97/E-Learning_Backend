# Generated by Django 4.2.3 on 2024-03-05 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0004_assessment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessment',
            name='pass_mark',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='total_points',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='assessment',
            name='total_question',
            field=models.IntegerField(),
        ),
    ]
