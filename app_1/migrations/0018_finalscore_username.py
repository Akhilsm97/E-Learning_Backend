# Generated by Django 4.2.3 on 2024-03-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0017_finalscore'),
    ]

    operations = [
        migrations.AddField(
            model_name='finalscore',
            name='username',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
