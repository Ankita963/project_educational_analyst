from django.db import models
from django import forms
from datetime import datetime,date


# Create your models here.
#'ENGINE':
#'django.db.backends.sqlite3'
#'NAME':BASE_DIR/'db.sqlite3',

class signuptab(models.Model):
    username=models.TextField(max_length=191)
    fname=models.TextField(max_length=191)
    lname=models.TextField(max_length=191)
    email=models.TextField(max_length=191)
    pass1=models.TextField(max_length=191)
    pass2=models.TextField(max_length=191)


class signintab(models.Model):
    username=models.TextField(max_length=191)
    pass1=models.TextField(max_length=191)


class uploadfolder(models.Model):
    """ my application """
    File_to_upload = models.FileField(upload_to='')
    

class uploadfileform(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

class createprofiletab(models.Model):
    user_id=models.TextField(max_length=50,null=True)
    fname=models.TextField(max_length=50)
    lname=models.TextField(max_length=50)
    dob=models.DateField()
    gender=models.CharField(max_length=6)
    ccode=models.IntegerField()
    phone=models.IntegerField()
    email=models.TextField(max_length=50)
    secemail=models.TextField(max_length=50)
    add=models.TextField(max_length=151)
    city=models.TextField(max_length=20)
    pin=models.IntegerField(null=True)
    state=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    hobbies=models.TextField(max_length=50)
    #models.ForeignKey(User, related_name='user_id')

    
class qualificationtab(models.Model):
    user_id=models.TextField(max_length=10,null=True)
    degree1=models.CharField(max_length=10,null=True)
    school1=models.TextField(max_length=50,null=True)
    board1=models.TextField(max_length=50,null=True)
    aos1=models.TextField(max_length=20,null=True)
    country1=models.TextField(max_length=20,null=True)
    state1=models.TextField(max_length=20,null=True)
    percentage1=models.IntegerField()
    dop1=models.DateField()
    file1 = models.FileField(upload_to='GFG/gfg/UploadDoc')

class qualificationtab1(models.Model):
    user_id=models.TextField(max_length=10)
    degreedetail2=models.TextField(max_length=20)
    degree2=models.CharField(max_length=10)
    school2=models.TextField(max_length=50)
    board2=models.TextField(max_length=50)
    aos2=models.TextField(max_length=20)
    country2=models.TextField(max_length=20)
    state2=models.TextField(max_length=20)
    percentage2=models.IntegerField()
    dop2=models.DateField()
    file2 = models.FileField(upload_to='GFG/gfg/UploadDoc')

class qualificationtab2(models.Model):
    user_id=models.TextField(max_length=10)
    degreedetail3=models.TextField(max_length=20)
    degree3=models.CharField(max_length=10)
    institute3=models.TextField(max_length=50)
    university3=models.TextField(max_length=50)
    aos3=models.TextField(max_length=20)
    country3=models.TextField(max_length=20)
    state3=models.TextField(max_length=20)
    percentage3=models.IntegerField()
    dop3=models.DateField()
    file3 = models.FileField(upload_to='GFG/gfg/UploadDoc') 

class qualificationtab3(models.Model):
    user_id=models.TextField(max_length=10)
    degreedetail4=models.TextField(max_length=20)
    degree4=models.CharField(max_length=10)
    institute4=models.TextField(max_length=50)
    university4=models.TextField(max_length=50)
    aos4=models.TextField(max_length=20)
    country4=models.TextField(max_length=20)
    state4=models.TextField(max_length=20)
    percentage4=models.IntegerField()
    dop4=models.DateField()
    file4 = models.FileField(upload_to='GFG/gfg/UploadDoc')


"""
class qualificationtab4(models.Model):
    backlog=models.CharField(max_length=10)
    hvgaps=models.CharField(max_length=10)
    gapmonth=models.TextField(max_lenth=20)
    gapreason=models.TextField(max_length=50)

"""

class patentstab(models.Model):
    user_id=models.TextField(max_length=10)
    patent_title=models.TextField(max_length=50)
    patent_no=models.TextField(max_length=50)
    patent_abstract=models.TextField(max_length=255)
    patent_inventors=models.TextField(max_length=100)
    patent_status=models.TextField(max_length=10)
    patent_filing_date=models.DateField()
    patent_proofoffiling=models.FileField(upload_to='GFG/gfg/UploadDoc')
    patent_publish_date=models.DateField()
    patent_proofofpublish=models.FileField(upload_to='GFG/gfg/UploadDoc')
    patent_issue_date=models.DateField()
    patent_proofofissue=models.FileField(upload_to='GFG/gfg/UploadDoc')
    patent_proofofacceptance=models.FileField(upload_to='GFG/gfg/UploadDoc')
    patent_document=models.FileField(upload_to='GFG/gfg/UploadDoc')


class certificatetab(models.Model):
    user_id=models.TextField(max_length=10)
    certificate_no=models.TextField(max_length=50)
    certified_by=models.TextField(max_length=100)
    certificate_reg_no=models.TextField(max_length=50)
    certificate_coursename=models.TextField(max_length=50)
    certificate_courseduration=models.TextField(max_length=50)
    certificate_gradeachieved=models.TextField(max_length=50)
    certificate_dateofissue=models.DateField()
    certificate_validtill=models.DateField()
    certificate_uploadcertificate=models.FileField(upload_to='GFG/gfg/UploadDoc')

"""
class researchpapertab(models.Model):
    user_id=models.TextField(max_length=10)
    research_papertitle=models.TextField(max_length=255)
    research_author=models.TextField(max_length=50)
    research_orcid=models.TextField(max_length=50)
    research_doi=models.TextField(max_length=50)
    research_emailofauthor=models.TextField(max_length=50)
    research_abstract=models.TextField(max_length=50)
    research_author=models.TextField(max_length=50)
    research_listofauthor=models.TextField(max_length=50)
    research_paper_area=models.TextField(max_length=50)
    research_affiliation=models.TextField(max_length=50)
    research_country=models.TextField(max_length=50)
    attach_researchpaper=models.FileField(upload_to='GFG/gfg/UploadDoc')
"""

class workexperiencetab(models.Model):
    user_id=models.TextField(max_length=10)
    work_organization=models.TextField(max_length=50)
    work_designation=models.TextField(max_length=50)
    work_from=models.DateField()
    work_to=models.DateField()
    work_responsibility=models.TextField(max_length=50)

class skilltab(models.Model):
    user_id=models.TextField(max_length=10)
    skill_title=models.TextField(max_length=50)
    skill_details=models.TextField(max_length=50)

class projecttab(models.Model):
    user_id=models.TextField(max_length=10)
    project_name=models.TextField(max_length=50)
    project_details=models.TextField(max_length=50)
    project_role=models.TextField(max_length=50)
    project_duration=models.TextField(max_length=50)
    team_size=models.TextField(max_length=50)

class achievementstab(models.Model):
    user_id=models.TextField(max_length=10)
    achievements_title=models.TextField(max_length=50)
    achievements_details=models.TextField(max_length=50)







    


    