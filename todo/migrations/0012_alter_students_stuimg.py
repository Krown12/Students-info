# Generated by Django 5.0 on 2023-12-27 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_rename_stu_photo_students_stuimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stuimg',
            field=models.ImageField(default=None, upload_to='students_picture'),
        ),
    ]