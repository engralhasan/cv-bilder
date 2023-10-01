from django.shortcuts import render,redirect,HttpResponse
import os
from .models import profile
from .pdf import html2pdf

# Create your views here.
def input(request):
    if request.method=="POST":
        lname = request.POST.get("lname")
        email = request.POST.get("email")
        age = request.POST.get("age")
        number = request.POST.get("number")
        address = request.POST.get("address")
        image = request.FILES.get("image")
        blood = request.POST.get("blood")
        nationality = request.POST.get("nationality")
        gender = request.POST.get("gender")
        relegion = request.POST.get("relegion")
        qualification = request.POST.get("qualification")
        date = request.POST.get("date")
        father_name = request.POST.get("father_name")
        mother_name = request.POST.get("mother_name")
        zip_cord = request.POST.get("zip_cord")
        # Work Experience one
        job1 = request.POST.get("job1")
        job2 = request.POST.get("job2")
        job3 = request.POST.get("job3")
        job4 = request.POST.get("job4")
        job5 = request.POST.get("job5")
        # Work Experience tow
        job6 = request.POST.get("job6")
        job7 = request.POST.get("job7")
        job8 = request.POST.get("job8")
        job9 = request.POST.get("job9")
        job10 = request.POST.get("job10")
        # Education one
        educ1 = request.POST.get("educ1")
        educ2 = request.POST.get("educ2")
        educ3 = request.POST.get("educ3")
        educ4 = request.POST.get("educ4")
        educ5 = request.POST.get("educ5")
        # Education tow
        educ6 = request.POST.get("educ6")
        educ7 = request.POST.get("educ7")
        educ8 = request.POST.get("educ8")
        educ9 = request.POST.get("educ9")
        educ10 = request.POST.get("educ10")
        
        # Portfolio one
        image1=request.FILES.get("image1")
        por1 = request.POST.get("portfolio_name1")
        por2 = request.POST.get("portfolio_details1")
        # Portfolio tow
        image2=request.FILES.get("image2")
        por3 = request.POST.get("portfolio_name2")
        por4 = request.POST.get("portfolio_details2")
        
        # References one
        image3=request.FILES.get("image3")
        ref1= request.POST.get("references_name1")
        ref2= request.POST.get("references_name2")
        ref3= request.POST.get("references_name3")
        ref4= request.POST.get("references_name4")
        # References tow
        image4=request.FILES.get("image")
        ref5= request.POST.get("references_name5")
        ref6= request.POST.get("references_name6")
        ref7= request.POST.get("references_name7")
        ref8= request.POST.get("references_name8")
        # Professional Skills
        skills1 = request.POST.get("skills1")
        skills2 = request.POST.get("skills2")
        skills3 = request.POST.get("skills3")
        skills4 = request.POST.get("skills4")
        skills5 = request.POST.get("skills5")
        skills6 = request.POST.get("skills6")
        skills7 = request.POST.get("skills7")
        skills8 = request.POST.get("skills8")
        skills9 = request.POST.get("skills9")
        skills10 = request.POST.get("skills10")
        skills11 = request.POST.get("skills11")
        skills12 = request.POST.get("skills12")
        skills13 = request.POST.get("skills13")
        skills14 = request.POST.get("skills14")
        skills15 = request.POST.get("skills15")
        skills16 = request.POST.get("skills16")
        

        
        
        if image :
            add = profile.objects.create(name=lname, email=email, age=age, number=number, 
                                     address=address, image=image, blood_group=blood, nationality=nationality,
                                     gender=gender, relegion=relegion, qualification=qualification,
                                     date_of_birth=date, father_name=father_name, mother_name=mother_name, zipd=zip_cord, job1=job1, job2=job2, job3=job3, job4=job4,
                                     job5=job5, job6=job6, job7=job7, job8=job8, job9=job9, job10=job10, 
                                     educ1=educ1, educ2=educ2, educ3=educ3, educ4=educ4, educ5=educ5,
                                     educ6=educ6, educ7=educ7, educ8=educ8, educ9=educ9, educ10=educ10,
                                     image1=image1, por1=por1, por2=por2, image2=image2, por3=por3, por4=por4,
                                     image3=image3, ref1=ref1, ref2=ref2, ref3=ref3, ref4=ref4,
                                     image4=image4, ref5=ref5, ref6=ref6, ref7=ref7, ref8=ref8,
                                     skills1=skills1, skills2=skills2, skills3=skills3, skills4=skills4, skills5=skills5,
                                     skills6=skills6, skills7=skills7, skills8=skills8, skills9=skills9, skills10=skills10,
                                     skills11=skills11, skills12=skills12, skills13=skills13, skills14=skills14, skills15=skills15,
                                     skills16=skills16)
            add.save() 
            return redirect(curd) 
            
        else:
            add = profile.objects.create(name=lname, email=email, age=age, number=number, 
                                     address=address,  blood_group=blood, nationality=nationality,
                                     gender=gender, relegion=relegion, qualification=qualification,
                                     date_of_birth=date, father_name=father_name, mother_name=mother_name,
                                     zipd=zip_cord, job1=job1,job2=job2,job3=job3,job4=job4,
                                     job5=job5,job6=job6,job7=job7,job8=job8,job9=job9,job10=job10, 
                                     educ1=educ1,educ2=educ2,educ3=educ3,educ4=educ4,educ5=educ5,
                                     educ6=educ6,educ7=educ7,educ8=educ8,educ9=educ9,educ10=educ10,
                                     image1=image1, por1=por1, por2=por2, image2=image2, por3=por3, por4=por4,
                                     image3=image3, ref1=ref1, ref2=ref2, ref3=ref3, ref4=ref4,
                                     image4=image4, ref5=ref5, ref6=ref6, ref7=ref7, ref8=ref8,
                                     skills1=skills1, skills2=skills2, skills3=skills3, skills4=skills4, skills5=skills5,
                                     skills6=skills6, skills7=skills7, skills8=skills8, skills9=skills9, skills10=skills10,
                                     skills11=skills11, skills12=skills12, skills13=skills13, skills14=skills14, skills15=skills15,
                                     skills16=skills16)
            add.save()
            return redirect(curd)
    
    return render(request,'home.html')

def curd(request):
    prof = profile.objects.all()
    prof = profile.objects.all()
    if request.method == 'GET':
        src = request.GET.get('src')
        if src:
            prof = profile.objects.filter(name__icontains=src)
        elif src == None:
            prof = profile.objects.all()
        else:
            prof = profile.objects.all()
    return render(request,'curd.html',{'prof':prof})

def cv(request, id):
    prof = profile.objects.get(id=id)
    return render(request,'index.html',locals())

def delete(request,id):
    prof = profile.objects.get(id=id)
    if prof.image != 'def.png':
        os.remove(prof.image.path)
    prof.delete()
    return redirect("curd")


def pdf(request,id):
    prof = profile.objects.get(id=id)
    pdf=html2pdf('pdf.html',{'prof':prof})
    return HttpResponse(pdf,content_type='application/pdf')