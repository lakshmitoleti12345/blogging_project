from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from .models import Contact
@login_required(login_url='login')
def HomePage(request):
   post=Contact.objects.all()
   return render(request,"home.html",{'post':post})
  
def SignupPage(request):
  if request.method=='POST':
    uname=request.POST.get('username')
    email=request.POST.get('email')
    pass1=request.POST.get('password1')
    pass2=request.POST.get('password2')
    if pass1 != pass2:
      return HttpResponse('your password and confirm password not same')
    else:
      my_user=User.objects.create_user(uname,email,pass1)
      my_user.save()
    return redirect('login')
  return render(request,'register.html')
def LoginPage(request):
  if request.method=='POST':
    username=request.POST.get('username')
    pass1=request.POST.get('pass')
    user=authenticate(request,username=username,password=pass1)
    if user is not None:
      login(request,user)
      return redirect('home')
    else:
      return HttpResponse('user name or password incorrect')
  return render(request,'login.html')
def LogoutPage(request):
  logout(request)
  return redirect('login')
@login_required(login_url='login')
def Blogging(request):

    if request.method == "POST":

        name = request.POST['name']
        email = request.POST['email']
        title = request.POST['title']
        message = request.POST['message']
        image = request.FILES.get('image')

        k = Contact(
            user=request.user,
            name=name,
            email=email,
            title=title,
            message=message,
            image=image
        )

        k.save()

        return redirect('home')

    return render(request,"blog_upload.html")
def upload(request):
   return redirect('blogupload')

def About(request):
   return render(request,'about.html')
@login_required(login_url='login')
def edit_post(request,id):

    post = Contact.objects.get(id=id,user=request.user)

    if request.method == "POST":
        post.title = request.POST['title']
        post.message = request.POST['message']
        post.save()

        return redirect('home')

    return render(request,'edit.html',{'post':post})


@login_required(login_url='login')
def delete_post(request,id):

    post = Contact.objects.get(id=id,user=request.user)

    post.delete()

    return redirect('home')

# Create your views here.

