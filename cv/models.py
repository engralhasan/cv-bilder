from django.db import models

# Create your models here.
class profile(models.Model):
    name= models.CharField(max_length=20)
    email=models.EmailField(max_length=50)
    age=models.PositiveIntegerField()
    number=models.TextField(max_length=15)
    address=models.TextField(max_length=200)
    image = models.ImageField(upload_to='prof_image/' ,default="def.png")
    blood_group = models.CharField(max_length=100)
    nationality=models.CharField(max_length=15)
    gender=models.CharField(max_length=100)
    relegion =models.CharField( max_length=7,null=True, blank=True)
    qualification=models.CharField(max_length=15)
    date_of_birth=models.CharField(max_length=15)
    father_name=models.CharField(max_length=15)
    mother_name=models.CharField(max_length=15)
    zipd=models.CharField(max_length=5,null=True, blank=True)
    # Work Experience one
    job1=models.CharField(max_length=50)
    job2=models.CharField(max_length=50)
    job3=models.CharField(max_length=15)
    job4=models.CharField(max_length=15)
    job5=models.CharField(max_length=1000)
    # Work Experience tow
    job6=models.CharField(max_length=50)
    job7=models.CharField(max_length=50)
    job8=models.CharField(max_length=15)
    job9=models.CharField(max_length=15)
    job10=models.CharField(max_length=1000)
    # Education one
    educ1=models.CharField(max_length=50)
    educ2=models.CharField(max_length=100)
    educ3=models.CharField(max_length=15)
    educ4=models.CharField(max_length=15)
    educ5=models.CharField(max_length=1000)
    # Education tow
    educ6=models.CharField(max_length=50)
    educ7=models.CharField(max_length=100)
    educ8=models.CharField(max_length=15)
    educ9=models.CharField(max_length=15)
    educ10=models.CharField(max_length=1000)
    # Portfolio one
    image1=models.ImageField(upload_to='prof1_image/' ,default="def.png")
    por1=models.CharField(max_length=100)
    por2=models.CharField(max_length=1000)
    # Portfolio tow
    image2=models.ImageField(upload_to='prof2_image/' ,default="def.png")
    por3=models.CharField(max_length=100)
    por4=models.CharField(max_length=1000)
    # References one
    image3=models.ImageField(upload_to='prof3_image/' ,default="def.png")
    ref1=models.CharField(max_length=50)
    ref2=models.CharField(max_length=100)
    ref3=models.CharField(max_length=100)
    ref4=models.CharField(max_length=1000)
    # References tow
    image4=models.ImageField(upload_to='prof4_image/' ,default="def.png")
    ref5=models.CharField(max_length=50)
    ref6=models.CharField(max_length=100)
    ref7=models.CharField(max_length=100)
    ref8=models.CharField(max_length=1000)
    
    # Professional Skills
    skills1=models.CharField(max_length=50,null=True, blank=True)
    skills2=models.CharField(max_length=3)
    skills3=models.CharField(max_length=50)
    skills4=models.CharField(max_length=3)
    skills5=models.CharField(max_length=50)
    skills6=models.CharField(max_length=3)
    skills7=models.CharField(max_length=50)
    skills8=models.CharField(max_length=3)
    skills9=models.CharField(max_length=50)
    skills10=models.CharField(max_length=3)
    skills11=models.CharField(max_length=50)
    skills12=models.CharField(max_length=3)
    skills13=models.CharField(max_length=50)
    skills14=models.CharField(max_length=3)
    skills15=models.CharField(max_length=50)
    skills16=models.CharField(max_length=3)
    

    
    def __str__(self) -> str:
        return self.name