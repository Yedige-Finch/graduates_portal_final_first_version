from django.db import models
from users.models import Employer,User,Student
from address.models import AddressField
# Create your models here.

GENDER_CHOICE={
    ('MALE', 'MALE'),
    ('FEMALE', 'FEMALE'),
}

EMPLOYMENT_CHOICE={
    ('Full employment', 'Full employment'),
    ('Part-time employment', 'Part-time employment'),
    ('Project work', 'Project work'),
    ('Volunteering', 'Volunteering'),
    ('Internship', 'Internship'),
}

SCHEDULE_CHOICE={
    ('Full day', 'Full day'),
    ('Shift work', 'Shift work'),
    ('Flexible schedule', 'Flexible schedule'),
    ('Remote work', 'Remote work'),
    ('Shift method', 'Shift method'),
}
class PhotoStudent(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	photo = models.ImageField(upload_to ='student/uploads/photo',default ='student/uploads/photo/default.png') 

class Portfolio(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	portfolio_photo = models.ImageField(null =True) 
	about_portfolio = models.TextField(null =True)

class PersonalInformation(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	name = models.CharField(max_length = 127,null=True)
	middle_name = models.CharField(max_length = 127,null=True)
	surname = models.CharField(max_length = 127,null=True)
	birthday = models.DateField(null=True)
	gender = models.CharField(max_length = 12,choices=GENDER_CHOICE,null=True)
	city = AddressField(null=True)

class ContactInformation(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	mobile_phone = models.CharField(max_length = 30,null=True,blank=True)
	home_phone = models.CharField(max_length = 30,null=True,blank=True)
	skype = models.CharField(max_length = 30,null=True,blank=True)

class DesiredPosition(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	desired_position = models.CharField(max_length = 30,null=True,blank=True)
	professional_area = models.CharField(max_length = 30,null=True,blank=True)
	employment = models.CharField(max_length = 100,choices=EMPLOYMENT_CHOICE,null=False,blank=True)
	schedule = models.CharField(max_length = 100,choices=SCHEDULE_CHOICE,null=False,blank=True)

class Experience(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	getting_started_date = models.DateField(null=True,blank=True)
	end_date = models.DateField(null=True,blank=True)
	organization = models.CharField(max_length = 100,null=True,blank=True)
	region = AddressField(null=True,blank=True)
	website = models.CharField(max_length = 100,null=True,blank=True)
	position = models.CharField(max_length = 100,null=True,blank=True)
	workplace_respon = models.TextField(null=True,blank=True)
	key_skills = models.CharField(max_length = 100,null=True,blank=True)

class AboutStudent(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_student = models.TextField(null=True)

class Education(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    faculty = models.CharField(max_length = 100,null=True)
    course = models.CharField(max_length = 100,null=True)
    specality = models.CharField(max_length = 100,null=True)
    date_of_ending = models.DateField(null=True)

class LanguageSkills(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    native_language = models.CharField(max_length = 100,null=True)
    second_language = models.CharField(max_length = 100,null=True,blank=True)


