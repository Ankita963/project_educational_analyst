from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from authentication import forms
from authentication.models import uploadfileform
from authentication.models import createprofiletab
from authentication.models import qualificationtab
from authentication.models import *
from django import forms
from django.core.files.storage import FileSystemStorage
from django.http import JsonResponse


# Create your views here.
def home(request):
    return render(request,'authentication/index.html')

def signup(request):

    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if User.objects.filter(username=username).first():
            messages.success(request,'username already exists')

            return redirect('/')
        if User.objects.filter(email=email).first():
            messages.success(request,'email is already exists')
            return redirect('/')

        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        if myuser.save() == True:
            messages.success(request, "Your Account has been successfully created.")
    
        

        return redirect('signin')
    return render(request,"authentication/signup.html")

    

def signin(request):

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']

       
        user = authenticate(username=username, password=pass1)
        

        if user is not None:
            login(request, user)
            fname = user.first_name
            request.session['userid'] = user.id
            #return render(request, "authentication/index.html", {'fname' : request.session['userid']})
            return redirect('/dashboard')

        else: 
            messages.error(request, "Bad Credentials!")
            return redirect('home')
        

    return render(request,"authentication/signin.html")



def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect('home')



def uploadfunc(request):
    if request.method=='POST':
        form =uploadfileform(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form=uploadfileform()
    return render(request,'authentication/upload.html', {'form':form})


def home_page_view(request):
    return render(request, "authentication/home.html") 


def createprofile(request):
    if request.method =='POST':
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        dob=request.POST.get('dob')
        gender=request.POST.get('gender')
        ccode=request.POST.get('ccode')
        phone=request.POST.get('phone')
        email=request.POST.get('email')
        secemail=request.POST.get('secemail')
        add=request.POST.get('add')
        city=request.POST.get('city')
        pin=request.POST.get('pin')
        state=request.POST.get('state')
        country=request.POST.get('country')
        hobbies=request.POST.get('hobbies')
        user_id=request.session['userid']
        en,created=createprofiletab.objects.update_or_create(
        user_id=request.session['userid'] ,
        defaults={'user_id':user_id, "fname":fname, "lname":lname, "dob":dob, "gender":gender, "ccode":ccode, "phone":phone, "email":email,"secemail":secemail,"add":add,"city":city,"pin":pin,"state":state,"country":country,"hobbies":hobbies},
        )
        #en=createprofiletab(user_id=user_id, fname=fname, lname=lname, dob=dob, gender=gender, ccode=ccode, phone=phone, email=email,secemail=secemail,add=add,city=city,pin=pin,state=state,country=country,hobbies=hobbies)
        en.save()
        return redirect('/qualification')
    return render(request, "authentication/createprofile.html")


def qualificationdetails(request):

    if request.method =='POST':
        upload_file_url=""
        user_id=request.session['userid']
        degree1=request.POST.get('degree1')
        school1=request.POST.get('school1')
        board1=request.POST.get('board1')
        aos1=request.POST.get('aos1')
        country1=request.POST.get('country1')
        state1=request.POST.get('state1')
        percentage1=request.POST.get('percentage1')
        dop1=request.POST.get('dop1')
        if len (request.FILES) != 0:
            
            file1=request.FILES['file1']
            fs=FileSystemStorage()
            filename=fs.save(file1.name,file1)
            upload_file_url = fs.url(file1)
            #print(upload_file_url)

        
        en=qualificationtab(user_id=user_id,degree1=degree1,school1=school1,board1=board1,aos1=aos1,country1=country1,state1=state1,percentage1=percentage1,dop1=dop1,file1=upload_file_url)
        en.save()
        return redirect('/qualification1')
        #messages.success(request,'form saved succesfully')
    return render(request,'authentication/qualification.html')

def qualificationdetails1(request):
    
    if request.method =='POST':
        user_id=request.session['userid']
        degreedetails2=request.POST.get('degreedetails2')
        degree2=request.POST.get('degree2')
        school2=request.POST.get('school2')
        board2=request.POST.get('board2')
        aos2=request.POST.get('aos2')
        country2=request.POST.get('country2')
        state2=request.POST.get('state2')
        percentage2=request.POST.get('percentage2')
        dop2=request.POST.get('dop2')
        if len (request.FILES) !=0:
            file2=request.FILES['file2']
            fs=FileSystemStorage()
            filename=fs.save(file1.name,file2)
            upload_file_url=fs.url(file2)
            print(upload_file_url)

        en=qualificationtab1(user_id=user_id,degree2=degree2,school2=school2,board2=board2,aos2=aos2,country2=country2,state2=state2,percentage2=percentage2,dop2=dop2,file2=upload_file_url)
        en.save()
        return redirect('/qualification2')
    

    return render(request,'authentication/qualification1.html')


def qualificationdetails2(request):
    
    if request.method =='POST':
        user_id=request.session['userid']
        degree3=request.POST.get('degree3')
        institute3=request.POST.get('school3')
        university3=request.POST.get('board3')
        aos3=request.POST.get('aos3')
        country3=request.POST.get('country3')
        state3=request.POST.get('state3')
        percentage3=request.POST.get('percentage3')
        dop3=request.POST.get('dop3')
        if len (request.FILES) !=0:
            file3=request.FILES['file3']
            fs=FileSystemStorage()
            filename=fs.save(file1.name,file3)
            upload_file_url=fs.url(file3)
            print(upload_file_url)

        en=qualificationtab2(user_id=user_id,degree3=degree3,school3=schoo3,board3=board3,aos3=aos3,country3=country3,state3=state3,percentage3=percentage3,dop3=dop3,file3=upload_file_url)
        en.save()
        return redirect('/qualification3')
       
    return render(request,'authentication/qualification2.html')

def qualificationdetails3(request):
    
    if request.method =='POST':
        user_id=request.session['userid']
        degree4=request.POST.get('degree4')
        institute4=request.POST.get('school4')
        university4=request.POST.get('board4')
        aos4=request.POST.get('aos4')
        country4=request.POST.get('country4')
        state4=request.POST.get('state4')
        percentage4=request.POST.get('percentage4')
        dop4=request.POST.get('dop4')
        if len (request.FILES) !=0:
            file4=request.FILES['file4']
            fs=FileSystemStorage()
            filename=fs.save(file4.name,file4)
            upload_file_url=fs.url(file4)
            print(upload_file_url)

        en=qualificationtab3(user_id=user_id,degree4=degree4,school4=schoo4,board4=board4,aos4=aos4,country4=country4,state4=state4,percentage4=percentage4,dop4=dop4,file4=upload_file_url)
        en.save()
        return redirect('/qualification4')
    
    return render(request,'authentication/qualification3.html')

def qualificationdetails4(request):
    """
    if request.method =='POST':
        user_id=request.session['userid']
        backlog=request.POST.get('backlog')
        hvgaps=request.POST.get('hvgaps')
        gapmonth=request.POST.get('gapmonth')
        gapreason=request.POST.get('gapreason')
        
        en=qualificationtab4(user_id=user_id,backlog=backlog,hvgaps=hvgaps,gapmonth=gapmonth,gapreason=gapreason)
        en.save()
        return redirect('/researchpaper')
    """
    return render(request,'authentication/qualification4.html')


def patents(request):
    if request.method =='POST':
        user_id=request.session['userid']
        patent_title=request.POST.get('patent_title')
        patent_no=request.POST.get('patent_no')
        patent_abstract=request.POST.get('patent_abstract')
        patent_inventors=request.POST.get('patent_inventors')
        patent_status=request.POST.get('patent_status')
        patent_filing_date=request.POST.get('patent_filing_date')
        if len (request.FILES) !=0:
            patent_proofoffiling=request.FILES['patent_proofoffiling']
            fs=FileSystemStorage()
            filename=fs.save(patent_proofoffiling.name,patent_proofoffiling)
            upload_file_url=fs.url(patent_proofoffiling)
            print(upload_file_url)
        patent_publish_date=request.POST.get('patent_publish_date')
        if len (request.FILES) !=0:
            patent_proofofpublish=request.FILES['patent_proofofpublish']
            fs=FileSystemStorage()
            filename=fs.save(patent_proofofpublish.name,patent_proofofpublish)
            upload_file_url=fs.url(patent_proofofpublish)
            print(upload_file_url)
        patent_issue_date=request.POST.get('patent_issue_date')
        if len (request.FILES) !=0:
            patent_proofofissue=request.FILES['patent_proofofissue']
            fs=FileSystemStorage()
            filename=fs.save(patent_proofofissue.name,patent_proofofissue)
            upload_file_url=fs.url(patent_proofofissue)
            print(upload_file_url)
        if len (request.FILES) !=0:
            patent_proofofacceptance=request.FILES['patent_proofofacceptance']
            fs=FileSystemStorage()
            filename=fs.save(patent_proofofacceptance.name,patent_proofofacceptance)
            upload_file_url=fs.url(patent_proofofacceptance)
            print(upload_file_url)
        if len (request.FILES) !=0:
            patent_document=request.FILES['patent_document']
            fs=FileSystemStorage()
            filename=fs.save(patent_document.name,patent_document)
            upload_file_url=fs.url(patent_document)
            print(upload_file_url)

        en=patentstab(user_id=user_id,patent_title=patent_title,patent_no=patent_no,patent_abstract=patent_abstract,
            patent_inventors=patent_inventors,patent_status=patent_status,patent_filing_date=patent_filing_date,patent_proofoffiling=patent_proofoffiling,
            patent_publish_date=patent_publish_date,patent_proofofpublish=patent_proofofpublish,patent_issue_date=patent_issue_date,
            patent_proofofissue=patent_proofofissue,patent_proofofacceptance=patent_proofofacceptance,patent_document=patent_document)
        en.save()
        return redirect('/certificate')

    return render(request,'authentication/patents.html')

def certificate(request):
    if request.method =='POST':
        user_id=request.session['userid']
        certificate_no=request.POST.get('certificate_no')
        certified_by=request.POST.get('certified_by')
        certificate_reg_no=request.POST.get('certificate_reg_no')
        certificate_coursename=request.POST.get('certificate_coursename')
        certificate_courseduration=request.POST.get('certificate_courseduration')
        certificate_gradeachieved=request.POST.get('certificate_gradeachieved')
        certificate_dateofissue=request.POST.get('certificate_dateofissue')
        certificate_validtill=request.POST.get('certificate_validtill')
        if len (request.FILES) !=0:
            certificate_uploadcertificate=request.FILES['certificate_uploadcertificate']
            fs=FileSystemStorage()
            filename=fs.save(certificate_uploadcertificate.name,certificate_uploadcertificate)
            upload_file_url=fs.url(certificate_uploadcertificate)
            print(upload_file_url)

        en=certificatetab(user_id=user_id,certificate_no=certificate_no,certified_by=certified_by,certificate_reg_no=certificate_reg_no,
            certificate_coursename=certificate_coursename,certificate_courseduration=certificate_courseduration,certificate_gradeachieved=certificate_gradeachieved,certificate_dateofissue=certificate_dateofissue,
            certificate_validtill=certificate_validtill,certificate_uploadcertificate=certificate_uploadcertificate)
        en.save()

    return render(request,'authentication/certificate.html')


def research_paper(request):
    """
    if request.method =='POST':
        user_id=request.session['userid']
        research_papertitle=request.POST.get('research_papertitle')
        research_author=request.POST.get('research_author')
        research_orcid=request.POST.get('research_orcid')
        research_doi=request.POST.get('research_doi')
        research_emailofauthor=request.POST.get('research_emailofauthor')
        research_abstract=request.POST.get('research_abstract')
        research_author=request.POST.get('research_author')
        research_listofauthor=request.POST.get('research_listofauthor')
        research_paper_area=request.POST.get('research_paper_area')
        research_affiliation=request.POST.get('research_affiliation')
        research_country=request.POST.get('research_country')
        if len (request.FILES) !=0:
            attach_researchpaper=request.FILES['attach_researchpaper']
            fs=FileSystemStorage()
            filename=fs.save(attach_researchpaper.name,attach_researchpaper)
            upload_file_url=fs.url(attach_researchpaper)
            print(upload_file_url)

        en=researchpapertab(user_id=user_id,research_papertitle=research_papertitle,research_author=research_author,
            research_orcid=research_orcid,research_doi=research_doi,research_emailofauthor=research_emailofauthor,
            research_abstract=research_abstract,research_author=research_author,research_listofauthor=research_listofauthor,
            research_paper_area=research_paper_area,research_affiliation=research_affiliation,
            research_country=research_country,attach_researchpaper=attach_researchpaper)
        en.save()
        """

    
    return render(request,'authentication/researchpaper.html')

def experience(request):

    if request.method =='POST':
        user_id=request.session['userid']
        work_organization=request.POST.get('work_organization')
        work_designation=request.POST.get('work_designation')
        work_from=request.POST.get('work_from')
        work_to=request.POST.get('work_to')
        work_responsibility=request.POST.get('work_responsibility')

        en=workexperiencetab(user_id=user_id,work_organization=work_organization,work_designation=work_designation,work_from=work_from,
            work_to=work_to,work_responsibility=work_responsibility)
        en.save()
    
    return render(request,'authentication/experience.html')


def project(request): 

    if request.method =='POST':
        user_id=request.session['userid']
        project_name=request.POST.get('project_name')
        project_details=request.POST.get('project_details')
        project_role=request.POST.get('project_role')
        project_duration=request.POST.get('project_duration')
        team_size=request.POST.get('team_size')

        en=projecttab(user_id=user_id,project_name=project_name,project_details=project_details,project_role=project_role,
            project_duration=project_duration,team_size=team_size)
        en.save()


    return render(request,'authentication/project.html')



def skills(request):

    if request.method =='POST':
        user_id=request.session['userid']
        skill_title=request.POST.get('skill_title')
        skill_details=request.POST.get('skill_details')

        en=skilltab(user_id=user_id,skill_title=skill_title,skill_details=skill_details)
        en.save()

    return render(request,'authentication/skills.html')

def achievements(request):

    if request.method =='POST':
        user_id=request.session['userid']
        achievements_title=request.POST.get('achievements_title')
        achievements_details=request.POST.get('achievements_details')

        en=achievementstab(user_id=user_id,achievements_title=achievements_title,achievements_details=achievements_details)
        en.save()


    return render(request,'authentication/achievements.html')



def createprofile_view(request):
    #std=createprofiletab.objects.all()
    #std=createprofiletab.objects.filter(fname__startswith='s')
    std=createprofiletab.objects.filter(user_id=request.session['userid'])
    return render(request,'authentication/createprofile_view.html',{'std':std})



def patents_view(request):
    std=patentstab.objects.filter(user_id=request.session['userid'])
    return render(request,'authentication/patents_view.html',{'std':std})



def certificate_view(request):
    std=certificatetab.objects.filter(user_id=request.session['userid'])
    return render(request,'authentication/certificate_view.html',{'std':std})






"""
def update_profile(request):
    args = {}

    if request.method == 'POST':
        form = UpdateProfile(request.POST)
        form.actual_user = request.user
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('update_profile_success'))
    else:
        form = UpdateProfile()

    args['form'] = form
    return render(request, 'registration/update_profile.html', args)

"""



"""def createprofileedit(request):
    return render(request, "authentication/createprofile_edit.html")"""



  
