# Generated by Django 4.0.1 on 2022-04-01 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='signin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=191)),
                ('pass1', models.TextField(max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='signup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.TextField(max_length=191)),
                ('fname', models.TextField(max_length=191)),
                ('lname', models.TextField(max_length=191)),
                ('email', models.TextField(max_length=191)),
                ('pass1', models.TextField(max_length=191)),
                ('pass2', models.TextField(max_length=191)),
            ],
        ),
        migrations.CreateModel(
            name='uploadfolder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('File_to_upload', models.FileField(upload_to='')),
            ],
        ),
    ]
