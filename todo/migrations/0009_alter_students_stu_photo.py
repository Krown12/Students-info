# Generated by Django 5.0 on 2023-12-27 14:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0008_students_stu_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stu_photo',
            field=models.ImageField(default=None, upload_to='students_picture'),
        ),
    ]