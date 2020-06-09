from django.shortcuts import render,render_to_response,redirect
from django.contrib.auth import logout, authenticate, login
from django.contrib import auth
from .forms import StudentForm,EmployerForm,UserForm
from .models import Student,Employer,User
from employer.models import Company
from django.contrib.auth.decorators import login_required
from main.decorators import student_required,employer_required
from django import forms
from student.models import PersonalInformation,ContactInformation,DesiredPosition,Experience,AboutStudent,Education,LanguageSkills,PhotoStudent
# Create your views here.


def logout(request):
	auth.logout(request)
	return redirect('main')

def login(request):
	context = {}
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None and user.is_active:
			if Student.objects.filter(user = User.objects.filter(username=username)[0]):
				if Student.objects.filter(user = User.objects.filter(username=username)[0])[0].сс_approve=='Y':
					auth.login(request,user)
					return redirect("student_home")
				else:
					context['text'] = 'Аккаунт еще не ободрен ЦК МУИТ'
					return render(request,"login.html",context)
			elif Employer.objects.filter(user = User.objects.filter(username=username)[0]) is not None:
				if Employer.objects.filter(user = User.objects.filter(username=username)[0])[0].сс_approve=='Y':
					auth.login(request,user)
					return redirect("employer_home")
				else:
					context['text'] = 'Аккаунт еще не ободрен ЦК МУИТ'
					return render(request,"login.html",context)
		else:
			context['text'] = 'Логин или пароль неправильный'
			return render(request,"login.html",context)
	elif request.user.is_authenticated and request.user.is_student:
		return redirect("student_home")
	elif request.user.is_authenticated and request.user.is_employer:
		return redirect("employer_home")
	return render(request,"login.html",context)


def registration_student(request):
	context = {}
	form = UserForm(request.POST or None)
	profile = StudentForm(request.POST or None)
	context['form'] = form
	context['profile'] = profile
	if request.method == "POST" and request.user.is_authenticated==False:
		if form.is_valid() and profile.is_valid():
			a = form.save()
			b = profile.save(commit=False)
			b.user = a
			b.save()
			user = User.objects.get(username=a)
			user.active=True
			user.is_student = True
			user.save()
			PersonalInformation.objects.create(user=a)
			DesiredPosition.objects.create(user=a)
			ContactInformation.objects.create(user=a)
			Experience.objects.create(user=a)
			AboutStudent.objects.create(user=a)
			Education.objects.create(user=a)
			LanguageSkills.objects.create(user=a)
			PhotoStudent.objects.create(user=a)
			return redirect("login")
	return render(request,"stud_form.html",context)

# not duplicating companies add
def registration_employer(request):
	context = {}
	form = UserForm(request.POST or None)
	profile = EmployerForm(request.POST or None)
	context['form'] = form
	context['profile'] = profile
	if request.method == "POST":
		if form.is_valid() and profile.is_valid():
			org_name = request.POST['org_name']
			if Employer.objects.filter(org_name=str(org_name)).exists():
				context['text'] = 'Such a company is already registered'
				return render(request,"employer_form.html",context)
			else:
				a = form.save()
				b = profile.save(commit=False)
				b.user = a
				b.save()
				user = User.objects.get(username=a)
				user.active=True
				user.is_employer = True
				user.save()
				Company.objects.create(employer=b)
				return redirect("login")
	return render(request,"employer_form.html",context)

