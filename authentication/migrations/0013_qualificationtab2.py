# Generated by Django 4.0.1 on 2022-04-23 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0012_qualificationtab1'),
    ]

    operations = [
        migrations.CreateModel(
            name='qualificationtab2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=10)),
                ('degreedetail3', models.TextField(max_length=20)),
                ('degree3', models.CharField(max_length=10)),
                ('institute3', models.TextField(max_length=50)),
                ('university3', models.TextField(max_length=50)),
                ('aos3', models.TextField(max_length=20)),
                ('country3', models.TextField(max_length=20)),
                ('state3', models.TextField(max_length=20)),
                ('percentage3', models.IntegerField()),
                ('dop3', models.DateField()),
                ('file3', models.FileField(upload_to='GFG/gfg/UploadDoc')),
            ],
        ),
    ]
