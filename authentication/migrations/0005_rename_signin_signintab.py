# Generated by Django 4.0.1 on 2022-04-15 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_rename_signup_signuptab'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='signin',
            new_name='signintab',
        ),
    ]