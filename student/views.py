from django.shortcuts import render,redirect,render_to_response,HttpResponse
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.db.models import Count
from django.forms import inlineformset_factory
from .models import PersonalInformation,ContactInformation,DesiredPosition,Experience,AboutStudent,Education,LanguageSkills,PhotoStudent
from .forms import PersonalInformationForm,ContactInformationForm,DesiredPositionForm,ExperienceForm,AboutStudentForm,EducationForm,LanguageSkillsForm,PhotoStudentForm,StudentEditForm,UserEditForm
from admin_override.models import Advice,Article
from admin_override import views
from employer.models import Vacancy,Company,Respond,FavoriteVacancy,UndesirableVacancy
from employer.forms import RespondFormStudent
from users.models import Employer,User,Student
from main.decorators import student_required,employer_required
from datetime import date, timedelta,datetime
import reportlab
from io import BytesIO
from reportlab.pdfgen import canvas


@login_required(redirect_field_name='login')
@student_required
def student_home(request):
	context = {}
	responds = Respond.objects.filter(student = request.user.student).count()
	favorite = FavoriteVacancy.objects.filter(student = request.user.student).count()
	undesirable = UndesirableVacancy.objects.filter(student = request.user.student).count()
	vacancies = Vacancy.objects.all()[:9]
	articles = Article.objects.all()[:3]
	advices = Advice.objects.all()[:3]
	companies = vacancies.values('company_name').annotate(total=Count('vacancy_name'))
	context['advices'] = advices
	context['companies'] = companies
	context['vacancies'] = vacancies
	context['user'] = request.user
	context['favorite'] = favorite
	context['undesirable'] = undesirable
	context['responds'] = responds
	context['articles'] = articles
	context['recommended_vacancy'] = recommendation(request)
	return render_to_response('student_home.html',context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(redirect_field_name='login')
@student_required
def resume_saved(request,saved=False):
	context = {}
	PersInforForm = PersonalInformationForm(request.POST or None, instance=request.user.personalinformation)
	ContInforForm = ContactInformationForm(request.POST or None, instance=request.user.contactinformation)
	DesiredForm = DesiredPositionForm(request.POST or None, instance=request.user.desiredposition)
	ExpForm = ExperienceForm(request.POST or None, instance=request.user.experience)
	AboutForm = AboutStudentForm(request.POST or None, instance=request.user.aboutstudent)
	EducForm = EducationForm(request.POST or None, instance=request.user.education)
	LangSkilForm = LanguageSkillsForm(request.POST or None, instance=request.user.languageskills)
	PhotoForm = PhotoStudentForm(request.POST or None, request.FILES, instance=request.user.photostudent)
	context['PersInforForm'] = PersInforForm
	context['ContInforForm'] = ContInforForm
	context['DesiredForm'] = DesiredForm
	context['ExpForm'] = ExpForm
	context['AboutForm'] = AboutForm
	context['EducForm'] = EducForm
	context['LangSkilForm'] = LangSkilForm
	context['PhotoForm'] = PhotoForm	
	context['saved'] = saved
	context['user'] = request.user
	return render(request,"resume.html",context)

@login_required
@student_required
def resume(request):
	context = {}	
	PersInforForm = PersonalInformationForm(request.POST or None, instance=request.user.personalinformation,initial={'name': request.user.first_name, 'surname':request.user.last_name})
	ContInforForm = ContactInformationForm(request.POST or None, instance=request.user.contactinformation)
	DesiredForm = DesiredPositionForm(request.POST or None, instance=request.user.desiredposition)
	ExpForm = ExperienceForm(request.POST or None, instance=request.user.experience)
	AboutForm = AboutStudentForm(request.POST or None, instance=request.user.aboutstudent)
	EducForm = EducationForm(request.POST or None, instance=request.user.education)
	LangSkilForm = LanguageSkillsForm(request.POST or None, instance=request.user.languageskills)
	PhotoForm = PhotoStudentForm(request.POST or None, request.FILES, instance=request.user.photostudent)
	context['PersInforForm'] = PersInforForm
	context['ContInforForm'] = ContInforForm
	context['DesiredForm'] = DesiredForm
	context['ExpForm'] = ExpForm
	context['AboutForm'] = AboutForm
	context['EducForm'] = EducForm
	context['LangSkilForm'] = LangSkilForm
	context['PhotoForm'] = PhotoForm
	context['user'] = request.user
	if PersInforForm.is_valid() and ContInforForm.is_valid() and DesiredForm.is_valid() and ExpForm.is_valid() and AboutForm.is_valid() and EducForm.is_valid() and LangSkilForm.is_valid():
		PersInforForm.save()
		ContInforForm.save()
		DesiredForm.save()
		ExpForm.save()
		AboutForm.save()
		EducForm.save()
		LangSkilForm.save()
		return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

@login_required
@student_required
def photo_student_save(request):
	context = {}
	PhotoForm = PhotoStudentForm(request.POST or None, request.FILES, instance=request.user.photostudent)
	context['PhotoForm'] = PhotoForm
	context['user'] = request.user
	if request.POST:
		if PhotoForm.is_valid():
			PhotoForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

@login_required
@student_required
def pers_inform_save(request):
	context = {}
	PersInforForm = PersonalInformationForm(request.POST or None, instance=request.user.personalinformation)
	context['PersInforForm'] = PersInforForm
	context['user'] = request.user
	if request.POST:
		if PersInforForm.is_valid():
			PersInforForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)


@login_required
@student_required
def contact_information_save(request):
	context = {}
	ContInforForm = ContactInformationForm(request.POST or None, instance=request.user.contactinformation)
	context['ContInforForm'] = ContInforForm
	context['user'] = request.user
	if request.POST:
		if ContInforForm.is_valid():
			ContInforForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)
	

@login_required
@student_required
def desired_position_save(request):
	context = {}
	DesiredForm = DesiredPositionForm(request.POST or None, instance=request.user.desiredposition)
	context['DesiredForm'] = DesiredForm
	context['user'] = request.user
	if request.POST:
		if DesiredForm.is_valid():
			DesiredForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

	

@login_required
@student_required
def experience_save(request):
	context = {}
	ExpForm = ExperienceForm(request.POST or None, instance=request.user.experience)
	context['ExpForm'] = ExpForm
	context['user'] = request.user
	if request.POST:
		if ExpForm.is_valid():
			ExpForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

@login_required
@student_required
def about_student_save(request):
	context = {}
	AboutForm = AboutStudentForm(request.POST or None, instance=request.user.aboutstudent)
	context['AboutForm'] = AboutForm
	context['user'] = request.user
	if request.POST:
		if AboutForm.is_valid():
			AboutForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

@login_required
@student_required
def education_save(request):
	context = {}
	EducForm = EducationForm(request.POST or None, instance=request.user.education)
	context['EducForm'] = EducForm
	context['user'] = request.user
	if request.POST:
		if EducForm.is_valid():
			EducForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)


@login_required
@student_required
def language_skills_save(request):
	context = {}
	LangSkilForm = LanguageSkillsForm(request.POST or None, instance=request.user.languageskills)
	context['LangSkilForm'] = LangSkilForm
	context['user'] = request.user
	if request.POST:
		if LangSkilForm.is_valid():
			LangSkilForm.save()
			return redirect("resume_saved",saved=True)
	return render(request,"resume.html",context)

@login_required
@student_required
def get_resume_student(request):
	age = ''
	context = {}
	context['user'] = request.user
	if PersonalInformation.objects.values('name').get(user=request.user)['name'] is not None:
		context['age'] = (date.today() - PersonalInformation.objects.values('birthday').get(user=request.user)['birthday']) // timedelta(days=365.2425)
		context['PersInfor'] = PersonalInformation.objects.get(user=request.user)
		context['ContInfor'] = ContactInformation.objects.get(user=request.user)
		context['DesrdPos'] = DesiredPosition.objects.get(user=request.user)	
		context['Expr'] = Experience.objects.get(user=request.user)
		context['AbtStudent'] = AboutStudent.objects.get(user=request.user)
		context['Edu'] = Education.objects.get(user=request.user)
		context['LangSkls'] = LanguageSkills.objects.get(user=request.user)
		context['photo'] = PhotoStudent.objects.get(user=request.user)
		vacancies = Vacancy.objects.all
		context['vacancies'] = vacancies
		context['recommended_vacancy'] = recommendation(request)
		context['key_skills'] = Experience.objects.values('key_skills').get(user=request.user)['key_skills'].split(',')
	else:
		return redirect("resume")
	return render_to_response('resume_main.html',context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required
@student_required
def photo_student(request):
	context = {}
	PhotoForm = PhotoStudentForm(request.POST or None,request.FILES, instance=request.user.photostudent)
	context['PhotoForm'] = PhotoForm
	context['user'] = request.user
	if request.POST:
		if PhotoForm.is_valid():
			PhotoForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

@login_required
@student_required
def pers_inform(request):
	context = {}
	PersInforForm = PersonalInformationForm(request.POST or None, instance=request.user.personalinformation)
	context['PersInforForm'] = PersInforForm
	context['user'] = request.user
	if request.POST:
		if PersInforForm.is_valid():
			PersInforForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

@login_required
@student_required
def contact_information(request):
	context = {}
	ContInforForm = ContactInformationForm(request.POST or None, instance=request.user.contactinformation)
	context['ContInforForm'] = ContInforForm
	context['user'] = request.user
	if request.POST:
		if ContInforForm.is_valid():
			ContInforForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)
	

@login_required
@student_required
def desired_position(request):
	context = {}
	DesiredForm = DesiredPositionForm(request.POST or None, instance=request.user.desiredposition)
	context['DesiredForm'] = DesiredForm
	context['user'] = request.user
	if request.POST:
		if DesiredForm.is_valid():
			DesiredForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

	

@login_required
@student_required
def experience(request):
	context = {}
	ExpForm = ExperienceForm(request.POST or None, instance=request.user.experience)
	context['ExpForm'] = ExpForm
	context['user'] = request.user
	if request.POST:
		if ExpForm.is_valid():
			ExpForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

@login_required
@student_required
def about_student(request):
	context = {}
	AboutForm = AboutStudentForm(request.POST or None, instance=request.user.aboutstudent)
	context['AboutForm'] = AboutForm
	context['user'] = request.user
	if request.POST:
		if AboutForm.is_valid():
			AboutForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

@login_required
@student_required
def education(request):
	context = {}
	EducForm = EducationForm(request.POST or None, instance=request.user.education)
	context['EducForm'] = EducForm
	context['user'] = request.user
	if request.POST:
		if EducForm.is_valid():
			EducForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)


@login_required
@student_required
def language_skills(request):
	context = {}
	LangSkilForm = LanguageSkillsForm(request.POST or None, instance=request.user.languageskills)
	context['LangSkilForm'] = LangSkilForm
	context['user'] = request.user
	if request.POST:
		if LangSkilForm.is_valid():
			LangSkilForm.save()
			return redirect("get_resume_student")
	return render(request,"all_type_resume.html",context)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
@login_required(redirect_field_name='login')
@student_required
def edit_student(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = StudentEditForm(request.POST or None, instance=request.user.student)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	return render(request,"edit_student_profile.html",context)

@login_required(redirect_field_name='login')
@student_required
def edited_student(request,saved=False):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = StudentEditForm(request.POST or None, instance=request.user.student)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	context['saved'] = saved
	return render(request,"edit_student_profile.html",context)

@login_required(redirect_field_name='login')
@student_required
def edit_student_user(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	context['form'] = form
	context['user'] = request.user
	context['form_active'] = True
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect("edited_student",saved=True)
	return render(request,"edit_student_profile.html",context)

@login_required(redirect_field_name='login')
@student_required(redirect_field_name='login')
def edit_student_profile(request):
	context = {}
	form = UserEditForm(request.POST or None, instance=request.user)
	profile = StudentEditForm(request.POST or None, instance=request.user.student)
	context['form'] = form
	context['profile'] = profile
	context['user'] = request.user
	if request.POST:
		if profile.is_valid():
			profile.save()
			return redirect("edited_student",saved=True)
	return render(request,"edit_student_profile.html",context)


# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------
# -------------------------------------------------------------------------------------------------------------------------------------------------------------

def vacancy_detail_get(request,vac_id):
	context = {}
	vacancies = Vacancy.objects.get(vac_id=vac_id)
	DesrdPos = DesiredPosition.objects.get(user=request.user)
	respond = Respond.objects.filter(vac_id=vac_id,student = request.user.student)
	favorite = FavoriteVacancy.objects.filter(vac_id=vac_id,student = request.user.student)
	undesirable = UndesirableVacancy.objects.filter(vac_id=vac_id,student = request.user.student)
	context['vacancies'] = vacancies
	context['DesrdPos'] = DesrdPos
	context['respond'] = respond
	context['favorite'] = favorite
	context['undesirable'] = undesirable
	return render(request,'vacancy_detail_student.html',context)

def company_detail_get(request,company_name):
	context = {}
	companies = Company.objects.get(company_name=company_name)
	company_name = Company.objects.values('company_name').get(company_name=company_name)['company_name']
	vacancies = Vacancy.objects.filter(company_name = company_name)
	context['companies'] = companies
	context['user'] = request.user
	context['vacancies'] = vacancies
	return render_to_response('company_detail_student.html',context)


@login_required
@student_required
def student_respond(request):
	vac_id = request.POST.get('vac_id',None)
	student = request.POST.get('student',None)
	message = request.POST['message']
	if request.POST:
		respond = Respond(vac_id = Vacancy(vac_id = vac_id), approve = False,student = request.user.student, message = message)
		respond.save()
		return redirect("responses_and_invitations")
	return redirect("student_home")

@login_required
@student_required
def add_to_favorite_vacancy(request):
	vac_id = request.POST.get('vac_id',None)
	student = request.POST.get('student',None)
	if request.POST:
		favorite = FavoriteVacancy(vac_id = Vacancy(vac_id = vac_id),student = request.user.student)
		favorite.save()
		return redirect("favorite_vacancies")
	return redirect("student_home")

@login_required
@student_required
def remove_from_favorite_vacancy(request):
	fav_id = request.POST.get('fav_id',None)
	student = request.POST.get('student',None)
	vac_id = request.POST.get('vac_id',None)
	if request.POST:
		favorite = FavoriteVacancy(fav_id = fav_id,vac_id = Vacancy(vac_id = vac_id),student = request.user.student)
		favorite.delete()
		return redirect("favorite_vacancies")
	return redirect("student_home")

@login_required
@student_required
def add_to_undesirable_vacancy(request):
	vac_id = request.POST.get('vac_id',None)
	student = request.POST.get('student',None)
	if request.POST:
		favorite = UndesirableVacancy(vac_id = Vacancy(vac_id = vac_id),student = request.user.student)
		favorite.save()
		return redirect("undesirable_vacancies")
	return redirect("student_home")

@login_required
@student_required
def remove_from_undesirable_vacancy(request):
	und_id = request.POST.get('und_id',None)
	student = request.POST.get('student',None)
	vac_id = request.POST.get('vac_id',None)
	if request.POST:
		favorite = UndesirableVacancy(und_id = und_id,vac_id = Vacancy(vac_id = vac_id),student = request.user.student)
		favorite.delete()
		return redirect("undesirable_vacancies")
	return redirect("student_home")

@login_required
@student_required
def responses_and_invitations(request):
	context = {}
	responds = Respond.objects.filter(student = request.user.student)
	vacancies = vacancy_of_the_day(request)
	context['responds'] = responds
	context['vacancies'] = vacancies
	context['user'] = request.user
	context['recommended_vacancy'] = recommendation(request)
	return render(request,'responses_and_invitations.html',context)

def recommendation(request):
	if DesiredPosition.objects.values('desired_position').get(user=request.user)['desired_position'] is not None:
		student_position = DesiredPosition.objects.values('desired_position').get(user=request.user)['desired_position']
		recommended_vacancy = Vacancy.objects.filter(
			Q(vacancy_name__icontains=student_position) | Q(about__icontains=student_position) | Q(Requirements__icontains=student_position)
			)
		return recommended_vacancy[:3]
	else:
		return None

@login_required
@student_required
def recommendation_all(request):
	context = {}
	if DesiredPosition.objects.values('desired_position').get(user=request.user)['desired_position'] is not None:
		student_position = DesiredPosition.objects.values('desired_position').get(user=request.user)['desired_position']
		recommended_vacancy = Vacancy.objects.filter(
			Q(vacancy_name__icontains=student_position) | Q(about__icontains=student_position) | Q(Requirements__icontains=student_position)
			)
		page = request.GET.get('page', 1)
		paginator = Paginator(recommended_vacancy, 5)
		try:
			recommended_vacancy = paginator.page(page)
		except PageNotAnInteger:
			recommended_vacancy = paginator.page(1)
		except EmptyPage:
			recommended_vacancy = paginator.page(paginator.num_pages)
		
		context['recommended_vacancies'] = recommended_vacancy
		return render(request,'list_vacancies.html',context)

@login_required
@student_required
def favorite_vacancies(request):
	context = {}
	favorite = FavoriteVacancy.objects.filter(student = request.user.student)
	vacancies = vacancy_of_the_day(request)	
	context['favorite'] = favorite
	context['vacancies'] = vacancies
	context['user'] = request.user
	context['recommended_vacancy'] = recommendation(request)
	return render(request,'favorite_vacancies.html',context)

@login_required
@student_required
def undesirable_vacancies(request):
	context = {}
	undesirable = UndesirableVacancy.objects.filter(student = request.user.student)
	vacancies = vacancy_of_the_day(request)
	context['undesirable'] = undesirable
	context['vacancies'] = vacancies
	context['user'] = request.user
	context['recommended_vacancy'] = recommendation(request)
	return render(request,'undesirable_vacancies.html',context)

@login_required
@student_required
def vacancy_of_the_day_all(request):
	context = {}
	today = datetime.now().date()
	recommended_vacancy = Vacancy.objects.filter(upd_date = today).all()
	page = request.GET.get('page', 1)
	paginator = Paginator(recommended_vacancy, 5)
	try:
		recommended_vacancy = paginator.page(page)
	except PageNotAnInteger:
		recommended_vacancy = paginator.page(1)
	except EmptyPage:
		recommended_vacancy = paginator.page(paginator.num_pages)
	
	context['recommended_vacancies'] = recommended_vacancy
	return render(request,'list_vacancies.html',context)

def vacancy_of_the_day(request):
	today = datetime.now().date()
	vacancies = Vacancy.objects.filter(upd_date = today)[:6]
	return vacancies
from reportlab.lib.colors import Color, black, blue, red

def some_view(request):
    pers = PersonalInformation.objects.get(user=request.user)
    photo = PhotoStudent.objects.get(user=request.user)
    ContInfor = ContactInformation.objects.get(user=request.user)
    DesrdPos = DesiredPosition.objects.get(user=request.user)	
    Expr = Experience.objects.get(user=request.user)
    AbtStudent = AboutStudent.objects.get(user=request.user)
    Edu = Education.objects.get(user=request.user)
    LangSkls = LanguageSkills.objects.get(user=request.user)
    photo = PhotoStudent.objects.get(user=request.user)

    nams = str(pers.surname + ' ' + pers.name + ' '  +  pers.middle_name)
    h_info = str(pers.gender + ',' + ' born ' + str(pers.birthday)) 
    ContInfor_pdf_phone = str('Phone: ' + str(ContInfor.mobile_phone))
    ContInfor_pdf_Home = str('Home phone: ' + str(ContInfor.home_phone))
    ContInfor_pdf_skype = str('Skype: ' + str(ContInfor.skype))

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="{}.pdf"'.format(nams)
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.drawString(200, 800,nams)
    p.drawString(200, 775, h_info)
    p.drawString(25, 700, ContInfor_pdf_phone)
    p.drawString(25, 675, ContInfor_pdf_Home)
    p.drawString(25, 650, ContInfor_pdf_skype)
    p.showPage()
    p.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response
