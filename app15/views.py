from django.shortcuts import render,redirect
from . forms import RegisterForm,LoginForm,UpdateForm,ChangePasswordForm,RegisterImageForm,LoginImageForm
from django .contrib import messages
from . models import Table1,Image
from django .contrib.auth import logout as logouts
# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        form=RegisterForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['place']
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            user=Table1.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,'user already exists')
                return redirect('/signup')
            elif password!=password:
                messages.warning(request,'mismatched')
                return redirect('/signup')
            else:
                tab=Table1(Name=name,Age=age,place=place,Email=email,Password=password)
                tab.save()
                messages.success(request,"complete")
                return redirect("/")
    else:
        form=RegisterForm()
    return render(request,'signup.html',{'data':form}) 







def login(request):
    if request.method=='POST':
        form=LoginForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Table1.objects.get(Email=email)

                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/login')
                elif password!=user.Password:
                    messages.warning(request,'incorrect password')
                    return redirect('/login')
                else:
                    messages.success(request,"login success")
                    return redirect("/home/%s" %user.id)
            except:
                messages.success(request,"incorrect email or password")
                return redirect("/login")
    else:
        form=LoginForm()
    return render(request,'login.html',{'data':form}) 

def home(request,id):
    user=Table1.objects.get(id=id)
    return render(request,'home.html',{'data':user})

def show_users(request):
    users=Table1.objects.all()
    return render(request,'show_users.html',{'data':users})

def update(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=UpdateForm(request.POST or None,instance=user)
        if form.is_valid():

         form.save()
         messages.success(request,"update succefully")
         return redirect('/show_users')

    else:
        form=UpdateForm(instance=user)
    return render(request,'update.html',{'user':user,'form':form})



def delete(request,id):
    user=Table1.objects.get(id=id)
    user.delete()
    messages.success(request,"delete succefully")
    return redirect('/show_users')

def changepassword(request,id):
    user=Table1.objects.get(id=id)
    if request.method=='POST':
        form=ChangePasswordForm(request.POST)
        if form.is_valid():
            oldpassword=form.cleaned_data['OldPassword']
            newpassword=form.cleaned_data['NewPassword']
            cpassword=form.cleaned_data['ConfirmPassword']
            if oldpassword!=user.Password:
                messages.warning(request,"password incorrect")
                return redirect('/changepassword/%s' % user.id)
            
            elif newpassword==oldpassword:
                messages.warning(request,'same password')
                return redirect('/changepassword/%s' % user.id)
            elif newpassword!=cpassword:
                    messages.warning(request,'incorrect password')
                    return redirect('/changepassword/%s' % user.id)


            else:
                    user.Password=newpassword
                    user.save()
                    messages.success(request,"password changed succefully")
                    return redirect("/login")
    else:
        form=ChangePasswordForm()
    return render(request,'changepassword.html',{'form':form,'user':user}) 





def registerimage(request):
    if request.method=='POST':
        form=RegisterImageForm(request.POST or None,request.FILES or None)
        if form.is_valid():
            name=form.cleaned_data['Name']
            age=form.cleaned_data['Age']
            place=form.cleaned_data['place']
            email=form.cleaned_data['Email']
            photo=form.cleaned_data['photo']
            password=form.cleaned_data['Password']
            cpassword=form.cleaned_data['ConfirmPassword']

            user=Image.objects.filter(Email=email).exists()

            if user:
                messages.warning(request,'user already exists')
                return redirect('/registerimage')
            elif password!=password:
                messages.warning(request,'mismatched')
                return redirect('/registerimage')
            else:
                tab=Image(Name=name,Age=age,place=place,photo=photo,Email=email,Password=password)
                tab.save()
                messages.success(request,"complete")
                return redirect("/")
    else:
        form=RegisterImageForm()
    return render(request,'registerimage.html',{'data':form})





def homeimage(request,id):
    user=Image.objects.get(id=id)
    return render(request,'homeimage.html',{'data':user})


def loginform(request):
    if request.method=='POST':
        form=LoginImageForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['Email']
            password=form.cleaned_data['Password']
            try:
                user=Table1.objects.get(Email=email)

                if not user:
                    messages.warning(request,'user does not exists')
                    return redirect('/loginimage')
                elif password!=user.Password:
                    messages.warning(request,'incorrect password')
                    return redirect('/loginimage')
                else:
                    messages.success(request,"login success")
                    return redirect("/home/%s" % user.id)
            except:
                messages.success(request,"incorrect email or password")
                return redirect("/loginimage")
    else:
        form=LoginForm()
    return render(request,'loginimage.html',{'data':form}) 





def logout(request):
    logouts(request)
    messages.success(request,'logout succeefull') 
    return redirect('/')