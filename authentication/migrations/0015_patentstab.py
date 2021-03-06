# Generated by Django 4.0.1 on 2022-04-25 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0014_qualificationtab3'),
    ]

    operations = [
        migrations.CreateModel(
            name='patentstab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.TextField(max_length=10)),
                ('patent_title', models.TextField(max_length=50)),
                ('patent_no', models.TextField(max_length=50)),
                ('patent_abstract', models.TextField(max_length=255)),
                ('patent_inventors', models.TextField(max_length=100)),
                ('patent_status', models.TextField(max_length=10)),
                ('patent_filing_date', models.DateField()),
                ('patent_proofoffiling', models.FileField(upload_to='GFG/gfg/UploadDoc')),
                ('patent_publish_date', models.DateField()),
                ('patent_proofofpublish', models.FileField(upload_to='GFG/gfg/UploadDoc')),
                ('patent_issue_date', models.DateField()),
                ('patent_proofofissue', models.FileField(upload_to='GFG/gfg/UploadDoc')),
                ('patent_proofofacceptance', models.FileField(upload_to='GFG/gfg/UploadDoc')),
                ('patent_document', models.FileField(upload_to='GFG/gfg/UploadDoc')),
            ],
        ),
    ]
