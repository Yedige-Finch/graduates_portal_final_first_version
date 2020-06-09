from django.db import models

# Create your models here.

class Advice(models.Model):
    adv_id = models.AutoField(primary_key=True)
    Advice = models.CharField(max_length = 512,null=False)
    photo = models.ImageField(upload_to ='admin_override/uploads/advice',null=False) 
    render = models.BooleanField(null = False,default = True)
    date = models.DateField(auto_now = True)

class Answers(models.Model):
	answer_help_type = models.CharField(max_length = 512,null=False)
	answer_question = models.CharField(max_length = 512,null=False) 
	answer = models.TextField(null=False)
	render = models.BooleanField(null = False,default = True)
	date = models.DateField(auto_now = True)

class Feedback(models.Model):
	topic = models.CharField(max_length = 512,null=False)
	content = models.TextField(null=False)
	sent_name = models.CharField(max_length = 512,null=False)
	e_mail = models.CharField(max_length = 512,null=False)
	date = models.DateField(auto_now = True)

class Article(models.Model):
	article_id = models.AutoField(primary_key=True)
	Author = models.CharField(max_length = 512,null=False)
	about_author = models.CharField(max_length = 512,null=False)
	photo = models.ImageField(upload_to ='admin_override/uploads/article',null=True)
	Theme = models.TextField(null=False)
	Article = models.TextField(null=False)
	Article_date = models.DateField(auto_now = False)
