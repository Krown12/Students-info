# Generated by Django 5.0 on 2023-12-23 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='students',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.TextField(max_length=100)),
                ('grade', models.TextField(choices=[(11, 'eleven'), (12, 'twelve')], max_length=2)),
                ('faculty', models.TextField(choices=[('science', 'science'), ('management', 'management'), ('commerce', 'commerce'), ('arts', 'arts')], max_length=12)),
            ],
        ),
    ]