from django.shortcuts import render,render_to_response,redirect
from .forms import UserEditForm,EmployerEditForm,CompanyEditForm,VacancyEditForm
from .models import Company,Vacancy,Respond
from users.models import User,Student
from django.contrib.auth.decorators import login_required
from main.decorators import student_required,employer_required
from django.contrib import messages
from student.models import PersonalInformation,ContactInformation,DesiredPosition,Experience,AboutStudent,Education,LanguageSkills
from datetime import date, timedelta

# Create your views here.
@login_required
@employer_required
def employer_home(request):
	context = {}
	context['user'] = request.user
	if Vacancy.objects.filter(employer = request.user.employer):
		vacancies = Vacancy.objects.filter(employer=request.user.employer).all()
		context['vacancies'] = vacancies
	else:
		vacancies = None
		context['vacancies'] = vacancies
	return render_to_response('employer_home.html',context)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@login_required(redirect_field_name='login')
@employer_required
def edit_employer(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = EmployerEditForm(request.POST or None, instance=request.user.employer)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	return render(request,"edit_employer_profile.html",context)

@login_required(redirect_field_name='login')
@employer_required
def edited_employer(request,saved=False):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = EmployerEditForm(request.POST or None, instance=request.user.employer)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	context['saved'] = saved
	return render(request,"edit_employer_profile.html",context)

@login_required(redirect_field_name='login')
@employer_required
def edit_employer_user(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	context['form'] = form
	context['user'] = request.user
	context['form_active'] = True
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect("edited_employer",saved=True)
	return render(request,"edit_employer_profile.html",context)

@login_required(redirect_field_name='login')
@employer_required
def edit_employer_profile(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = EmployerEditForm(request.POST or None, instance=request.user.employer)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	if request.POST:
		if profile.is_valid():
			profile.save()
			return redirect("edited_employer",saved=True)
	return render(request,"edit_employer_profile.html",context)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@login_required(redirect_field_name='login')
@employer_required
def company(request):
	context = {}
	company = CompanyEditForm(request.POST or None,instance=request.user.employer.company,initial={'company_name': request.user.employer.org_name, 'company_mail':request.user,'contacts_phone':request.user.employer.phone})
	context['company'] = company
	context['user'] = request.user
	if request.POST:
		if company.is_valid():
			company.save()
			return redirect("edited_company",saved=True)
	return render(request,"form_comp_vac.html",context)

@login_required(redirect_field_name='login')
@employer_required
def edited_company(request,saved=False):
	context = {}
	company = CompanyEditForm(request.POST or None, instance=request.user.employer.company)
	context['company'] = company
	context['user'] = request.user
	context['saved'] = saved
	return render(request,"form_comp_vac.html",context)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@login_required(redirect_field_name='login')
@employer_required
def vacancy(request):
	if Company.objects.values('company_name').get(employer=request.user.employer)['company_name'] is not None:
		context = {}
		vacancy = VacancyEditForm(request.POST or None,initial={'contact_mail': request.user})
		context['vacancy'] = vacancy
		context['user'] = request.user
		if request.POST:
			if vacancy.is_valid():
				new_record = vacancy.save(commit = False)
				new_record.employer = request.user.employer
				new_record.company_name = request.user.employer.org_name
				new_record.save()
				return redirect("employer_home")
		return render(request,"form_comp_vac.html",context)
	else:
		messages.info(request, 'First Edit company information')
		return redirect("company")

@login_required(redirect_field_name='login')
@employer_required
def remove_vacancy(request,vac_id):
	vacancy = Vacancy(vac_id = vac_id,employer = request.user.employer)
	vacancy.delete()
	return redirect("employer_home")

@login_required(redirect_field_name='login')
@employer_required
def edited_vacancy(request,saved=False):
	context = {}
	vacancy = VacancyEditForm(request.POST or None)
	context['vacancy'] = vacancy
	context['user'] = request.user
	context['saved'] = saved
	return render(request,"form_comp_vac.html",context)

@login_required(redirect_field_name='login')
@employer_required
def vacancy_edit(request,vac_id):
	context = {}
	vacancies = Vacancy.objects.get(vac_id = vac_id)
	vacancy = VacancyEditForm(request.POST or None,instance= vacancies)
	context['vacancy'] = vacancy
	context['vac_id'] = vac_id
	context['user'] = request.user
	if request.POST:
		if vacancy.is_valid():
			vacancy.save()
			next = request.POST.get('next', '/')
			return redirect(next)
	return render(request,"vacancy_edit.html",context)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
@login_required
@employer_required
def company_get(request):
	context = {}
	if Company.objects.values('company_name').get(employer=request.user.employer)['company_name'] is not None:
		company = Company.objects.get(employer=request.user.employer)
		company_name = Company.objects.values('company_name').get(employer=request.user.employer)['company_name']
		vacancies = Vacancy.objects.filter(company_name = company_name)
		context['vacancies'] = vacancies
		context['user'] = request.user
		context['company'] = company
		return render_to_response('company.html',context)
	else:
		return redirect("company")

def candidates(request):
	context = {}
	vacancies = Vacancy.objects.filter(employer=request.user.employer)
	vac_ids = vacancies.values_list('vac_id')
	responds = Respond.objects.filter(vac_id__in=vac_ids)
	context['responds'] = responds
	context['vacancies'] = vacancies	
	return render(request,'candidates.html',context)
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

@login_required
@employer_required
def vacancy_get(request):
	context = {}
	context['user'] = request.user
	return render_to_response('vacancy.html',context)

def vacancy_detail_employer(request,vac_id):
	context = {}
	vacancies = Vacancy.objects.get(vac_id=vac_id)
	responds = Respond.objects.filter(vac_id=vac_id).all()
	context['vacancies'] = vacancies
	context['responds'] = responds
	context['user'] = request.user
	return render_to_response('vacancy_detail.html',context)

# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------
# --------------------------------------------------------------------------------------------------------

@login_required
@employer_required
def resume_employer(request):
	context['user'] = request.user
	return render_to_response('get_resume_student.html')

@login_required
@employer_required
def get_resume_student(request,user,resp_id):
	user = User.objects.get(username = user)
	student = Student.objects.get(user = user)
	age = (date.today() - PersonalInformation.objects.values('birthday').get(user=user)['birthday']) // timedelta(days=365.2425)
	PersInfor = PersonalInformation.objects.get(user=user)
	ContInfor = ContactInformation.objects.get(user=user)
	DesrdPos = DesiredPosition.objects.get(user=user)	
	Expr = Experience.objects.get(user=user)
	AbtStudent = AboutStudent.objects.get(user=user)
	Edu = Education.objects.get(user=user)
	LangSkls = LanguageSkills.objects.get(user=user)
	responds = Respond.objects.get(student = student,resp_id = resp_id)
	if responds.respond_status_student == 'Resume not viewed':
		responds.respond_status_student = 'Resume viewed'
		responds.save()
	key_skills = Experience.objects.values('key_skills').get(user=user)['key_skills'].split(',')
	return render(request,'get_resume_student.html',
		{'user_last_login':User.objects.get(username=request.user).last_login,
		'age':age,
		'PersInfor': PersInfor,
		'ContInfor': ContInfor,
		'DesrdPos': DesrdPos,
		'Expr': Expr,
		'AbtStudent': AbtStudent,
		'Edu': Edu,
		'LangSkls': LangSkls,
		'user':request.user,
		'responds':responds,
		'key_skills':key_skills
		})


@login_required
@employer_required
def reject_student(request):
	resp_id = request.POST.get('resp_id',None)
	employer_message = request.POST['employer_message']
	if request.POST:
		responds = Respond.objects.get(resp_id=resp_id)
		responds.approve = False
		responds.employer_message = employer_message
		responds.respond_status_student = 'Renouncement'
		responds.save()
	return redirect('candidates')

@login_required
@employer_required
def invite_student(request):
	resp_id = request.POST.get('resp_id',None)
	employer_message = request.POST['employer_message']
	if request.POST:
		responds = Respond.objects.get(resp_id=resp_id)
		responds.approve = True
		responds.employer_message = employer_message
		responds.respond_status_student = 'Invititation'
		responds.save()
	return redirect("candidates")