# Generated by Django 4.2.3 on 2024-03-26 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0014_completedvideos'),
    ]

    operations = [
        migrations.AddField(
            model_name='completedvideos',
            name='username',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
