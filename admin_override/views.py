from django.shortcuts import render,redirect,render_to_response
from django.contrib.auth.decorators import login_required
from main.decorators import student_required,employer_required
from .models import Advice,Answers,Feedback,Article
from .forms import FeedbackForm
from users.models import Employer,User,Student
from django.forms import inlineformset_factory
from datetime import date, timedelta
from django.db.models.query import QuerySet
# Create your views here.


def get_answers(request):
	context = {}	
	results = Answers.objects.order_by('answer_help_type')
	context['results'] = results
	print(results)
	return render(request,"help.html",context)

def feedback(request):
	context = {}
	if request.user.is_authenticated:
		form = FeedbackForm(request.POST or None,initial={'e_mail': request.user, 'sent_name':request.user.first_name + ' ' + request.user.last_name })
	else:
		form = FeedbackForm(request.POST or None)
	context['form'] = form
	if request.POST:
		if form.is_valid():
			form.save()
			return redirect("feedback_saved",saved=True)
	return render(request,"feedback.html",context)

def feedback_saved(request,saved=False):
	context = {}
	if request.user.is_authenticated:
		form = FeedbackForm(request.POST or None,initial={'e_mail': request.user, 'sent_name':request.user.first_name + ' ' + request.user.last_name })
	else:
		form = FeedbackForm(request.POST or None)
	context['form'] = form
	context['saved'] = saved
	return render(request,"feedback.html",context)

def software_requirements(request):
	return render(request,"software_requirements.html")

def new(request):
	return render(request,"software_requirements.html")

def news(request,article_id):
	context = {}
	article = Article.objects.get(article_id = article_id)
	articles = Article.objects.all()[:3]
	context['article'] = article
	context['articles'] = articles
	return render(request,"news.html",context)
