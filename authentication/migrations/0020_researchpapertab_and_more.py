# Generated by Django 4.0.1 on 2022-05-08 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_achievementstab_achievements_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='researchpapertab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=10)),
                ('research_papertitle', models.TextField(max_length=255)),
                ('research_author', models.TextField(max_length=50)),
                ('research_orcid', models.TextField(max_length=50)),
                ('research_doi', models.TextField(max_length=50)),
                ('research_emailofauthor', models.TextField(max_length=50)),
                ('research_abstract', models.TextField(max_length=50)),
                ('research_listofauthor', models.TextField(max_length=50)),
                ('research_paper_area', models.TextField(max_length=50)),
                ('research_affiliation', models.TextField(max_length=50)),
                ('research_country', models.TextField(max_length=50)),
                ('attach_researchpaper', models.FileField(upload_to='')),
                ('proof_of_acceptance', models.FileField(upload_to='')),
            ],
        ),
        migrations.AlterField(
            model_name='certificatetab',
            name='certificate_uploadcertificate',
            field=models.FileField(upload_to=''),
        ),
    ]