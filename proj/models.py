from django.db import models
import os
import datetime


#-------------------------------------------------------------------------------------------------function to handle image
def filepath(req,filename):
   old_filename = filename
   timeNow = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
   filename= "%s%s" % (timeNow,old_filename)
   return os.path.join('uploads/',filename)



#--------------------------------------------------------------------------------------------------------------table to store manager details

class signup(models.Model):
  
    name=models.CharField(max_length=25)
    Mname=models.CharField(max_length=25)
    mobile=models.CharField(max_length=12,unique=True)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    pincode=models.CharField(max_length=10)
    email=models.CharField(max_length=50,unique=True)
    password=models.CharField(max_length=25)



#--------------------------------------------------------------------------------------------------------------table to store employee details who have register 
class empsignup(models.Model):
  
    empname=models.CharField(max_length=25)
    empMname=models.CharField(max_length=25)
    empmobile=models.CharField(max_length=12,unique=True)
    empcity=models.CharField(max_length=50)
    empstate=models.CharField(max_length=50)
    emppincode=models.CharField(max_length=10)
    empemail=models.CharField(max_length=50,unique=True)
    emppassword=models.CharField(max_length=25)
    status=models.CharField(max_length=5,null=True,blank=True)


#--------------------------------------------------------------------------------------------------------------table to store employee details who are accepted by manager
class acceptemp(models.Model):

    empname=models.CharField(max_length=25)
    empMname=models.CharField(max_length=25)
    empmobile=models.CharField(max_length=12,unique=True)
    empcity=models.CharField(max_length=50)
    empstate=models.CharField(max_length=50)
    emppincode=models.CharField(max_length=10)
    empemail=models.CharField(max_length=50,unique=True)
    emppassword=models.CharField(max_length=25)
    status=models.CharField(max_length=5,null=True,blank=True)


#--------------------------------------------------------------------------------------------------------------table to store company details

class maindetails(models.Model):
  
    Cname=models.CharField(max_length=25)
    Mnumber=models.CharField(max_length=15)
    email=models.CharField(max_length=50)
    city=models.CharField(max_length=50,null=True,blank=True)


#--------------------------------------------------------------------------------------------------------------table to store home section details
class Home(models.Model):
    box1=models.CharField(max_length=50)
    box2=models.CharField(max_length=50)
    box3=models.CharField(max_length=50)
    box4=models.CharField(max_length=50)


#--------------------------------------------------------------------------------------------------------------table to store service section details
class Services(models.Model):

   heading=models.CharField(max_length=50)
   subheading=models.CharField(max_length=50)
   ser1=models.CharField(max_length=100)
   ser2=models.CharField(max_length=100)
   ser3=models.CharField(max_length=100)
   ser4=models.CharField(max_length=100)
   ser5=models.CharField(max_length=100)
   Simage=models.ImageField(upload_to=filepath,null=True,blank=True)



#--------------------------------------------------------------------------------------------------------------table to store about section details   
class About(models.Model):
   
   Aimage=models.ImageField(upload_to=filepath,null=True,blank=True)
   heading=models.CharField(max_length=50)
   subheading=models.CharField(max_length=50)
   para=models.CharField(max_length=600)
   bellpara=models.CharField(max_length=200,null=True,blank=True)
   chartpara=models.CharField(max_length=200,null=True,blank=True)
   phone=models.CharField(max_length=15,null=True,blank=True)



#--------------------------------------------------------------------------------------------------------------table to store elements section details
class Elements(models.Model):
   
   mainHead=models.CharField(max_length=50)

   box1head=models.CharField(max_length=50)
   box2head=models.CharField(max_length=50)
   box3head=models.CharField(max_length=50)
   box4head=models.CharField(max_length=50) 
   
   box1para=models.CharField(max_length=300)
   box2para=models.CharField(max_length=300)
   box3para=models.CharField(max_length=300)
   box4para=models.CharField(max_length=300)
 
   mainHead2=models.CharField(max_length=50)
   Eimage=models.ImageField(upload_to=filepath,null=True,blank=True)
   prohead1=models.CharField(max_length=50)
   prohead2=models.CharField(max_length=50)
   prohead3=models.CharField(max_length=50)
   prohead4=models.CharField(max_length=50)



#--------------------------------------------------------------------------------------------------------------table to store blog section details
class Blog(models.Model):
   
   heading=models.CharField(max_length=30)
  
   Bimage1=models.ImageField(upload_to=filepath,null=True,blank=True)
   Bimage2=models.ImageField(upload_to=filepath,null=True,blank=True)
   Bimage3=models.ImageField(upload_to=filepath,null=True,blank=True)
   Bimage4=models.ImageField(upload_to=filepath,null=True,blank=True)
   Bimage5=models.ImageField(upload_to=filepath,null=True,blank=True)
   Bimage6=models.ImageField(upload_to=filepath,null=True,blank=True)

   subhead1=models.CharField(max_length=50)
   subhead2=models.CharField(max_length=50)
   subhead3=models.CharField(max_length=50)
   subhead4=models.CharField(max_length=50)
   subhead5=models.CharField(max_length=50)
   subhead6=models.CharField(max_length=50)

   desc1=models.CharField(max_length=100)
   desc2=models.CharField(max_length=100)
   desc3=models.CharField(max_length=100)
   desc4=models.CharField(max_length=100)
   desc5=models.CharField(max_length=100)
   desc6=models.CharField(max_length=100)


#--------------------------------------------------------------------------------------------------------------table to store footer section details
class Default(models.Model):
   
   Cdesc=models.CharField(max_length=300)
   Ulinkhead1=models.CharField(max_length=30)
   Ulinkhead2=models.CharField(max_length=30)
   Ulinkhead3=models.CharField(max_length=30)
   Ulinkhead4=models.CharField(max_length=30)
   Ulinkhead5=models.CharField(max_length=30)

   Ulink1=models.CharField(max_length=2048)
   Ulink2=models.CharField(max_length=2048)
   Ulink3=models.CharField(max_length=2048)
   Ulink4=models.CharField(max_length=2048)
   Ulink5=models.CharField(max_length=2048)


#--------------------------------------------------------------------------------------------------------------table to store details come from contect form
class Contact(models.Model):
    
   name=models.CharField(max_length=40)
   phone=models.CharField(max_length=15)
   email=models.CharField(max_length=40)
   subject=models.CharField(max_length=40)
   message=models.CharField(max_length=1000)