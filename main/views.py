from django.shortcuts import render,render_to_response,redirect
from employer.models import Vacancy,Company
from django.db.models import Q,Count
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from admin_override.models import Advice,Article

def main(request):
	context = {}
	vacancies = Vacancy.objects.all()[:9]
	articles = Article.objects.all()[:3]
	companies = vacancies.values('company_name').annotate(total=Count('vacancy_name'))
	context['vacancies'] = vacancies
	context['articles'] = articles
	context['companies'] = companies
	return render(request,'main.html',context)

def get_vacancy_main(request):
	vacancies = Vacancy.objects.all()
	return render_to_response('main.html',{'vacancies': vacancies})

def get_company_main(request):
	companies = Company.objects.get(company_name=company_name)
	return render_to_response('main.html',{'vacancies': companies})

def vacancy_detail_get(request,vac_id):
	vacancies = Vacancy.objects.get(vac_id=vac_id)
	return render_to_response('vacancy_detail_main.html',{'vacancies': vacancies})

def company_detail_get(request,company_name):
	context = {}
	companies = Company.objects.get(company_name=company_name)
	company_name = Company.objects.values('company_name').get(company_name=company_name)['company_name']
	vacancies = Vacancy.objects.filter(company_name = company_name)
	context['vacancies'] = vacancies
	context['companies'] = companies
	return render_to_response('company_detail_main.html',context)

def search_vacancy(request):
	context = {}
	query = request.GET['search_word']
	search_results = Vacancy.objects.filter(
		Q(vacancy_name__icontains=query) | Q(about__icontains=query) | Q(Requirements__icontains=query)|Q(company_name__icontains=query)
		)
	page = request.GET.get('page', 1)
	paginator = Paginator(search_results, 5)
	try:
		search_results = paginator.page(page)
	except PageNotAnInteger:
		search_results = paginator.page(1)
	except EmptyPage:
		search_results = paginator.page(paginator.num_pages)
	context['search_results'] = search_results
	if request.user.is_authenticated and request.user.is_student:
		return render(request,'vacancy_list_student.html',context)
	else:
		return render(request,'vacancy_list.html',context)