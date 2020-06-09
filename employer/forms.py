from django import forms
from django.forms import ModelForm
from users.models import Employer,User
from .models import Company,Vacancy,Respond
from django.contrib.auth.forms import UserCreationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class UserEditForm(ModelForm):
	old_password = forms.CharField(required=False,label='Старый пароль')
	password = forms.CharField(required=False,label='Новый пароль')
	def clean_password(self):
		phone = self.cleaned_data.get('password')
		if len(phone)!=0 and len(phone)<7:
			raise forms.ValidationError('Пароль должен состоять из не менее 7 символов')
		return phone
	def clean_old_password(self):
		phone = self.cleaned_data.get('old_password')
		if len(phone)!=0 and len(phone)<7:
				raise forms.ValidationError('Пароль должен состоять из не менее 7 символов')
		return phone
	def clean(self):
		user = User.objects.get(username = self.instance)
		password = self.cleaned_data.get('password')
		old_password = self.cleaned_data.get('old_password')
		if password!=None and old_password==None:
			raise forms.ValidationError('Введите старый пароль!')
		if password==None and old_password!=None:
			raise forms.ValidationError('Введите новый пароль!')
		if password!="" or old_password!="":
			if not user.check_password(old_password):
				raise forms.ValidationError('Старый пароль неверный!')
			else:
				if password=="":
					raise forms.ValidationError('Введите новый пароль!')
				if password==old_password:
					raise forms.ValidationError('Новый пароль должен отличаться от старого!')
	
	def __init__(self, *args, **kwargs):
		super(UserEditForm, self).__init__(*args, **kwargs)
		for field in self.fields.values():
			field.widget.attrs['class'] = 'form-control'	

	class Meta:
	    model = User
	    fields = ('first_name','last_name')

	def save(self, commit=True):
		user = super(UserEditForm, self).save(commit=False)
		u = self.instance
		password = self.cleaned_data.get('password')
		old_password = self.cleaned_data.get('old_password')
		if password!=old_password and password!="" and old_password!="":
			if user.check_password(old_password):
				user.set_password(password)
		if commit:
			user.save()
			return user


class EmployerEditForm(ModelForm):
    class Meta:
        model = Employer
        fields = ('org_name','position','phone')
    def __init__(self, *args, **kwargs):
        super(EmployerEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class CompanyEditForm(ModelForm):
    class Meta:
        model = Company
        exclude = ('comp_id','employer',)
    def __init__(self, *args, **kwargs):
        super(CompanyEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class VacancyEditForm(ModelForm):
    class Meta:
        model = Vacancy
        exclude = ('vac_id','employer','company_name')
    def __init__(self, *args, **kwargs):
        super(VacancyEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class RespondFormStudent(ModelForm):
    class Meta:
        model = Respond
        fields = ('message',)
    def __init__(self, *args, **kwargs):
        super(RespondFormStudent, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'	