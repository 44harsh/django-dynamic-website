from django.shortcuts import render,redirect
from django.db.utils import IntegrityError
from django.http import HttpResponse
from.models import signup,maindetails,empsignup,Home,About,Elements,Blog,Default,Services,Contact,acceptemp

global record
record=maindetails.objects.filter(id=1)

global defrec
defrec=Default.objects.filter(id=1)

def defau(req):
  defrec=Default.objects.filter(id=1)
  return render(req,'default.html',{'defrec':defrec})




#------------------------------------------------------------------------------------------------------------------------------function to update footer section
 
def defdata(req):     
  if req.method=="GET":
   defrec=Default.objects.filter(id=1)
   return render(req,'defdata.html',{'defrec':defrec})
  else:
   ob=Default()
   defrec=Default.objects.filter(id=1)
   ob.id=1
   ob.Cdesc=req.POST.get('Cdesc')
   ob.Ulinkhead1=req.POST.get('Ulinkhead1')
   ob.Ulinkhead2=req.POST.get('Ulinkhead2')
   ob.Ulinkhead3=req.POST.get('Ulinkhead3')
   ob.Ulinkhead4=req.POST.get('Ulinkhead4')
   ob.Ulinkhead5=req.POST.get('Ulinkhead5')
   ob.Ulink1=req.POST.get('Ulink1')
   ob.Ulink2=req.POST.get('Ulink2')
   ob.Ulink3=req.POST.get('Ulink3')
   ob.Ulink4=req.POST.get('Ulink4')
   ob.Ulink5=req.POST.get('Ulink5')
   ob.save()
   msg="successfully done"
   return render(req,'defdata.html',{'msg':msg,'emprec':emprec,'defrec':defrec})

def home(req):
   homerec=Home.objects.filter(id=1)
   return render(req,'home.html',{'record':record,'homerec':homerec,'defrec':defrec})



#-----------------------------------------------------------------------------------------------------------------------------function to update home section

def homedata(req):
   if req.method=="GET":
     homerec=Home.objects.filter(id=1)
     return render(req,'homedata.html',{'homerec':homerec})
   else:
     ob=Home()
     homerec=Home.objects.filter(id=1)
     ob.id=1
     ob.box1=req.POST.get('box1')
     ob.box2=req.POST.get('box2')
     ob.box3=req.POST.get('box3')
     ob.box4=req.POST.get('box4')
     ob.save()
     msg="succesfully done"
     return render(req,'homedata.html',{'msg':msg,'emprec':emprec,'homerec':homerec})

def about(req):
   aboutrec=About.objects.filter(id=1)
   return render(req,'about.html',{'record':record,'defrec':defrec,'aboutrec':aboutrec})





#--------------------------------------------------------------------------------------------------------------------------------function to update about section

def aboutdata(req):
   if req.method=="GET":
      aboutrec=About.objects.filter(id=1)
      return render(req,'aboutdata.html',{'aboutrec':aboutrec})
   else:
     ob=About()
     aboutrec=About.objects.filter(id=1)
     ob.id=1
     ob.heading=req.POST.get('heading')
     ob.subheading=req.POST.get('subheading')
     ob.para=req.POST.get('para')
     ob.bellpara=req.POST.get('bellpara')
     ob.chartpara=req.POST.get('chartpara')
     ob.phone=req.POST.get('phone')
     if len(req.FILES)!=0:
         ob.Aimage=req.FILES['Aimage']
     ob.save()
     msg="successfully done"
     return render(req,'aboutdata.html',{'msg':msg,'emprec':emprec,'aboutrec':aboutrec})

def services(req):
   serrec=Services.objects.filter(id=1)
   return render(req,'Services.html',{'record':record,'defrec':defrec,'serrec':serrec})




#------------------------------------------------------------------------------------------------------------------------------function to update services section
   
def servicesdata(req):
   if req.method=="GET":
     serrec=Services.objects.filter(id=1)
     return render(req,'servicesdata.html',{'serrec':serrec})
   else:
     ob=Services()
     serrec=Services.objects.filter(id=1)
     ob.id=1
     ob.heading=req.POST.get('heading')
     ob.subheading=req.POST.get('subheading')
     ob.ser1=req.POST.get('ser1')
     ob.ser2=req.POST.get('ser2')
     ob.ser3=req.POST.get('ser3')
     ob.ser4=req.POST.get('ser4')
     ob.ser5=req.POST.get('ser5')
     if len(req.FILES)!=0:
         ob.Simage=req.FILES['Simage']
     ob.save()
     msg="successfully done"
     return render(req,'servicesdata.html',{'msg':msg,'emprec':emprec,'serrec':serrec})

def elements(req):
   elerec=Elements.objects.filter(id=1)
   return render(req,'elements.html',{'record':record,'defrec':defrec,'elerec':elerec})


#---------------------------------------------------------------------------------------------------------------------------------function to update element section

def elementsdata(req):
   if req.method=="GET":
     elerec=Elements.objects.filter(id=1)
     return render(req,'elementsdata.html',{'elerec':elerec})
   else:
     ob=Elements()
     elerec=Elements.objects.filter(id=1)
     ob.id=1
     ob.mainHead=req.POST.get('mainHead')
     ob.box1head=req.POST.get('box1head')
     ob.box2head=req.POST.get('box2head')
     ob.box3head=req.POST.get('box3head')
     ob.box4head=req.POST.get('box4head')
     ob.box1para=req.POST.get('box1para')
     ob.box2para=req.POST.get('box2para')
     ob.box3para=req.POST.get('box3para')
     ob.box4para=req.POST.get('box4para')
     ob.mainHead2=req.POST.get('mainHead2')
     if len(req.FILES)!=0:
         ob.Eimage=req.FILES['Eimage']
     ob.prohead1=req.POST.get('prohead1')
     ob.prohead2=req.POST.get('prohead2')
     ob.prohead3=req.POST.get('prohead3')
     ob.prohead4=req.POST.get('prohead4')
     ob.save()
     msg="successfully done"
     return render(req,'elementsdata.html',{'msg':msg,'emprec':emprec,'elerec':elerec})

def blog(req):
   blorec=Blog.objects.filter(id=1)
   return render(req,'blog.html',{'record':record,'defrec':defrec,'blorec':blorec})


#---------------------------------------------------------------------------------------------------------------------------------function to update blog section

def blogdata(req):
   if req.method=="GET":
      blorec=Blog.objects.filter(id=1)
      return render(req,'blogdata.html',{'blorec':blorec})
   else:
      ob=Blog()
      blorec=Blog.objects.filter(id=1)
      ob.id=1
      ob.heading=req.POST.get('heading')
      if len(req.FILES)!=0:
         ob.Bimage1=req.FILES['Bimage1']
      if len(req.FILES)!=0:
         ob.Bimage2=req.FILES['Bimage2']
      if len(req.FILES)!=0:
         ob.Bimage3=req.FILES['Bimage3']
      if len(req.FILES)!=0:
         ob.Bimage4=req.FILES['Bimage4']
      if len(req.FILES)!=0:
         ob.Bimage5=req.FILES['Bimage5']
      if len(req.FILES)!=0:
         ob.Bimage6=req.FILES['Bimage6']
      ob.subhead1=req.POST.get('subhead1')
      ob.subhead2=req.POST.get('subhead2')
      ob.subhead3=req.POST.get('subhead3')
      ob.subhead4=req.POST.get('subhead4')
      ob.subhead5=req.POST.get('subhead5')
      ob.subhead6=req.POST.get('subhead6')
      ob.desc1=req.POST.get('desc1')
      ob.desc2=req.POST.get('desc2')
      ob.desc3=req.POST.get('desc3')
      ob.desc4=req.POST.get('desc4')
      ob.desc5=req.POST.get('desc5')
      ob.desc6=req.POST.get('desc6')
      ob.save()
      msg="sucessfully done"
      return render(req,'blogdata.html',{'msg':msg,'emprec':emprec,'blorec':blorec})


#-----------------------------------------------------------------------------------------------------------------------function to save data send from contact form

def contact(req):
  if req.method=="GET":
      return render(req,'contact.html',{'record':record,'defrec':defrec})
  else:
     ob=Contact()
     ob.name=req.POST.get('name')
     ob.phone=req.POST.get('phone')
     ob.email=req.POST.get('email')
     ob.subject=req.POST.get('subject')
     ob.message=req.POST.get('message')
     ob.save()
     return render(req,'contact.html',{'record':record,'defrec':defrec})



#-----------------------------------------------------------------------------------------------------------------------function to get message information

def contactdata(req):
   id=req.GET.get('id')
   emprec=acceptemp.objects.filter(id=id)
   con=Contact.objects.all()
   return render(req,'contactdata.html',{'con':con,'emprec':emprec})

   
def logout(req):
  return redirect(log)

def emplogout(req):
  return redirect(emplog)


#--------------------------------------------------------------------------------------------------------------------------------------function for manager login

def log(req):
  if req.method=="GET": 
    return render(req,'login.html')      
  else:
   email=req.POST.get('email')
   password=req.POST.get('pass')
   
   ob=signup() 
   ob.email=email
   ob.password=password
   msgg="Password or email is wrong"
   global rec
   global newrec
   rec=signup.objects.filter(email=email,password=password)
   newrec=maindetails.objects.filter(id=1)
   if(rec):
       return render(req,'profile.html',{'rec':rec,'newrec':newrec})
   else:
       return render(req,'login.html',{'msgg':msgg})


#------------------------------------------------------------------------------------------------------------------------------------function for employee login

def emplog(req):
  if req.method=="GET": 
    return render(req,'emplogin.html')      
  else:
   empemail=req.POST.get('email')
   emppassword=req.POST.get('pass')
   
   ob=acceptemp() 
   ob.empemail=empemail
   ob.emppassword=emppassword
   msgg="Password or email is wrong"
   global emprec
   emprec=acceptemp.objects.filter(empemail=empemail,emppassword=emppassword)
   if(emprec):
       return render(req,'empprofile.html',{'emprec':emprec})
   else:
       return render(req,'emplogin.html',{'msgg':msgg})



#----------------------------------------------------------------------------------------------------------------------------------function to update employee details

def empup(req):

 if req.method=="GET":
  id=req.GET.get('id')
  emprec=empsignup.objects.filter(id=id)
  return render(req,'empup.html',{'emprec':emprec})
 else:
  ob=empsignup()
  id=req.POST.get('id')
  emprec=empsignup.objects.filter(id=id)
  ob.id=id
  ob.empname=req.POST.get('empname')
  ob.empMname=req.POST.get('empMname')
  ob.empmobile=req.POST.get('empmobile')
  ob.empcity=req.POST.get('empcity')
  ob.empstate=req.POST.get('empstate')
  ob.emppincode=req.POST.get('emppincode')
  ob.empemail=req.POST.get('empemail')
  ob.emppassword=req.POST.get('emppassword')
  ob.save()
  msg="Successfully done"
  return render(req,'empup.html',{'msg':msg,'emprec':emprec})



#---------------------------------------------------------------------------------------------------------------------------------function to registration of employee

def regis(req):
   code=req.GET.get('err')
   msg=""
   if code=="0":
     msg="done"
     homerec=Home.objects.filter(id=1) 
     return render(req,'home.html',{'record':record,'defrec':defrec,'homerec':homerec})
   if code=="1":
     msg="User already exist"
   if code=="2":
     msg="fail!" 
   return render(req,"signup.html",{"msg":msg})

def registration(req):	
 if req.method=="GET": 
    return render(req,"signup.html")      
 else:
  code=0
  try: 
   name=req.POST.get('nam')
   Mname=req.POST.get('mother')
   mobile=req.POST.get('mobile')
   city=req.POST.get('city')
   state=req.POST.get('state')
   pincode=req.POST.get('pincode')
   email=req.POST.get('email')
   password=req.POST.get('pass')
   ob=empsignup()
   ob.empname=name
   ob.empMname=Mname
   ob.empmobile=mobile
   ob.empcity=city
   ob.empstate=state
   ob.emppincode=pincode
   ob.empemail=email
   ob.emppassword=password
   ob.status=0;
   ob.save()
  except IntegrityError:
   code=1
  except Exception as ex:
   code=2  
  return redirect("/regis?err="+str(code))


def comup(req):
  return render(req,'manup.html',{'rec':rec,'newrec':newrec})


def pro(req):
  lid=req.GET.get('id')
  rec=signup.objects.filter(id=lid)
  return render(req,'profile.html',{'rec':rec,'newrec':newrec})

def emppro(req):
  lid=req.GET.get('lid')
  emprec=empsignup.objects.filter(id=lid)
  return render(req,'empprofile.html',{'emprec':emprec})


#---------------------------------------------------------------------------------------------------------------------------------function to update company details

def comname(req):
  Cname=req.POST.get('Cname')
  email=req.POST.get('email')
  city=req.POST.get('city')
  Mnumber=req.POST.get('Mnumber')
  
  ob=maindetails()
  newrec=maindetails.objects.filter(id=1)
  ob.id=1
  ob.Cname=Cname
  ob.Mnumber=Mnumber
  ob.email=email
  ob.city=city
  ob.save()
  msg="Successfully done"
  return render(req,'manup.html',{'msg':msg,'newrec':newrec,'rec':rec})


#----------------------------------------------------------------------------------------------function to show employee details which have register through website

def empdetails(req):

 if req.method=="GET":
  empdelrec=empsignup.objects.all()
  return render(req,'empdet.html',{'empdelrec':empdelrec,'rec':rec})
 else:
  ob=acceptemp()
  ob.id=req.POST.get('id')
  ob.empname=req.POST.get('empname')
  ob.empMname=req.POST.get('empMname')
  ob.empmobile=req.POST.get('empmobile')
  ob.empcity=req.POST.get('empcity')
  ob.empstate=req.POST.get('empstate')
  ob.emppincode=req.POST.get('emppincode')
  ob.empemail=req.POST.get('empemail')
  ob.emppassword=req.POST.get('emppassword')
  ob.status=1;
  ob.save()
  empdelrec=empsignup.objects.all()
  msg="Successfully done"
  return render(req,'profile.html',{'rec':rec,'newrec':newrec,'msg':msg})  



#------------------------------------------------------------------------------------------------------------function to show employee which are accepted by manager

def acceptedemp(req):
   accemp=acceptemp.objects.all()
   return render(req,'acceptedemp.html',{'accemp':accemp,'rec':rec})




#------------------------------------------------------------------------------------------------------------function to remove employee by manager
def removeemp(req):
   id=req.POST.get('id')
   ob=acceptemp.objects.filter(id=id).delete()
   accemp=acceptemp.objects.all()
   return render(req,'acceptedemp.html',{'accemp':accemp}) 
  	


#---------------------------------------------------------------------------------------------------------------------------------function to update manager details

def managerup(req):

 if req.method=="GET":
  lid=req.GET.get('id')
  emp=signup.objects.filter(id=lid)
  return render(req,'ManProUp.html',{'emp':emp})
 else:
  mid=req.POST.get('id')
  name=req.POST.get('name')
  Mname=req.POST.get('Mname')
  mobile=req.POST.get('mobile')
  city=req.POST.get('city')
  state=req.POST.get('state')
  pincode=req.POST.get('pincode')
  email=req.POST.get('email')
  password=req.POST.get('password')
 
  ob=signup()
  emp=signup.objects.filter(id=mid)
  ob.id=mid
  ob.name=name
  ob.Mname=Mname
  ob.mobile=mobile
  ob.city=city
  ob.state=state
  ob.pincode=pincode
  ob.email=email
  ob.password=password
  ob.save()
  msg="Successfully done"
  return render(req,'ManProUp.html',{'msg':msg,'emp':emp})

#--------------------------------------------------------------------------------------------------------------------------------------------END