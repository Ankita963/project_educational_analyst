# Generated by Django 4.0.1 on 2022-04-11 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_qualification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='qualification',
            name='file1',
            field=models.FileField(upload_to='GFG/UploadDoc'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='file2',
            field=models.FileField(upload_to='GFG/UploadDoc'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='file3',
            field=models.FileField(upload_to='GFG/UploadDoc'),
        ),
        migrations.AlterField(
            model_name='qualification',
            name='file4',
            field=models.FileField(upload_to='GFG/UploadDoc'),
        ),
    ]