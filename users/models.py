from django.db import models
from django.contrib.auth.models import AbstractUser

SPECIALITY_CHOICE={
    ('CSSE', 'CSSE'),
    ('IS', 'IS'),
    ('RET', 'RET'),
}
COURSE_CHOICES={
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),

}
APPROVE_CHOICES={
    ('N', 'N'),
    ('Y', 'Y'),
}
# Create your models here.
class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_employer = models.BooleanField(default=False)

# добавить дату рождения
class Student(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    student_id = models.CharField(max_length = 12,null=False,)
    course = models.CharField(max_length = 1,choices = COURSE_CHOICES,null=False)
    speciality = models.CharField(max_length = 12,choices=SPECIALITY_CHOICE,null=False)
    phone = models.CharField(max_length = 12,null=False)
    сс_approve = models.CharField(max_length = 1,choices=APPROVE_CHOICES,null=True,default='N')

class Employer(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    org_name = models.CharField(max_length = 72,null=False)
    position = models.CharField(max_length = 24,null=False)
    phone = models.CharField(max_length = 12,null=False)
    сс_approve = models.CharField(max_length = 1,choices=APPROVE_CHOICES,null=True,default='N')
