# Generated by Django 5.0 on 2023-12-27 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0014_alter_students_stuimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='stuimg',
            field=models.ImageField(null=True, upload_to='students_picture/'),
        ),
    ]