# Generated by Django 5.0 on 2023-12-27 09:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_students_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='nationality',
        ),
        migrations.AlterField(
            model_name='students',
            name='description',
            field=models.TextField(max_length=150),
        ),
    ]