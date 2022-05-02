# Generated by Django 4.0.1 on 2022-04-21 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_qualificationtab_delete_qualification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='qualificationtab',
            name='aos',
        ),
        migrations.AddField(
            model_name='qualificationtab',
            name='aos1',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='qualificationtab',
            name='user_id',
            field=models.TextField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='qualificationtab',
            name='board1',
            field=models.TextField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='qualificationtab',
            name='country1',
            field=models.TextField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='qualificationtab',
            name='degree1',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='qualificationtab',
            name='state1',
            field=models.TextField(max_length=20, null=True),
        ),
    ]
