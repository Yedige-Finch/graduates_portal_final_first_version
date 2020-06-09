from django.db import models
from users.models import User,Employer
from address.models import AddressField
from users.models import Student

respond_status={
    ('1', 'Resume not viewed'),
    ('2', 'Resume viewed'),
    ('3', 'Invite'),
    ('4', 'Renouncement'),
}
class Company(models.Model):
	company_id = models.AutoField(primary_key=True)
	company_name = models.CharField(max_length = 512,null=True)
	company_mail = models.CharField(max_length = 512,null=True)
	about_company = models.TextField(null=True)
	address = AddressField(null=True)
	contacts_phone = models.CharField(max_length = 512,null=True)
	contacts_site = models.CharField(max_length = 512,null=True)
	industry = models.TextField(null=True)
	employer = models.OneToOneField(Employer, on_delete=models.CASCADE)

class Vacancy(models.Model):
	vac_id = models.AutoField(primary_key=True)
	vacancy_name = models.CharField(max_length = 512,null=True)
	salary = models.CharField(max_length = 512,null=True)
	company_name = models.CharField(max_length = 512,null=True)
	address = AddressField(null=True)
	experience = models.TextField(null=True)
	# schedule = models.CharField(max_length = 512,null=True)
	about = models.TextField(null=True)
	duties = models.TextField(null=True)
	Requirements = models.TextField(null=True)
	work_condition = models.TextField(null=True)
	skills = models.TextField(null=True)
	contacts_phone = models.CharField(max_length = 512,null=True)
	contact_mail = models.CharField(max_length = 512,null=True)
	publication_date = models.DateField(auto_now_add=True,null=True)
	upd_date = models.DateField(auto_now =True,null=True)
	employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
	
class Respond(models.Model):
	resp_id = models.AutoField(primary_key=True)
	approve = models.BooleanField()
	send_date = models.DateField(auto_now =True)
	message = models.TextField(null=True,blank = True)
	employer_message = models.TextField(null=True,blank = True)
	respond_status_student = models.CharField(max_length = 512,default='Resume not viewed')
	respond_status_employer = models.CharField(max_length = 512,null=True)
	respond_send_date = models.DateField(auto_now =True,null=True)
	vac_id =  models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	student =  models.ForeignKey(Student, on_delete=models.CASCADE)

class FavoriteVacancy(models.Model):
	fav_id = models.AutoField(primary_key=True)
	vac_id =  models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	student =  models.ForeignKey(Student, on_delete=models.CASCADE)

class UndesirableVacancy(models.Model):
	und_id = models.AutoField(primary_key=True)
	vac_id =  models.ForeignKey(Vacancy, on_delete=models.CASCADE)
	student =  models.ForeignKey(Student, on_delete=models.CASCADE)

class FavoriteCompany(models.Model):
	fav_id = models.AutoField(primary_key=True)
	company_id =  models.ForeignKey(Company, on_delete=models.CASCADE)
	student =  models.ForeignKey(Student, on_delete=models.CASCADE)


class UndesirableCompany(models.Model):
	und_id = models.AutoField(primary_key=True)
	company_id =  models.ForeignKey(Company, on_delete=models.CASCADE)
	student =  models.ForeignKey(Student, on_delete=models.CASCADE)
