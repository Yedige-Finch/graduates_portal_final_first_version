from django import forms
from django.forms import ModelForm
from .models import PersonalInformation,ContactInformation,DesiredPosition,Experience,AboutStudent,Education,LanguageSkills,PhotoStudent
from users.models import User,Student
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Submit, HTML, Button, Row, Field

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name')

    def __init__(self, *args, **kwargs):
        super(ContactInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def save(self, commit=True):
        user = super(UserForm, self).save(commit=False)
        u = self.instance
        if commit:
            user.save()
            return user

class PersonalInformationForm(ModelForm):
    class Meta:
        model = PersonalInformation
        widgets = {
        'birthday': forms.DateInput(attrs={'type': 'date'}),
        }
        exclude = ('user',)
    
    def __init__(self, *args, **kwargs):
        super(PersonalInformationForm, self).__init__(*args, **kwargs)
        self.fields['gender'].widget.attrs['id'] = "inputState"
        self.fields['birthday'].widget.attrs['id'] = 'date-input'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'



class ContactInformationForm(ModelForm):
    class Meta:
        model = ContactInformation
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(ContactInformationForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class DesiredPositionForm(ModelForm):
    class Meta:
        model = DesiredPosition
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(DesiredPositionForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class ExperienceForm(ModelForm):
    class Meta:
        model = Experience
        exclude = ('user',)
        widgets = {
        'getting_started_date': forms.DateInput(attrs={'type': 'date'}),
        'end_date': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(ExperienceForm, self).__init__(*args, **kwargs)
        self.fields['getting_started_date'].widget.attrs['id'] = 'date-input'
        self.fields['end_date'].widget.attrs['id'] = 'date-input'
        self.fields['website'].widget.attrs['id'] = 'url'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class AboutStudentForm(ModelForm):
    class Meta:
        model = AboutStudent
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(AboutStudentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class EducationForm(ModelForm):
    class Meta:
        model = Education
        exclude = ('user',)
        widgets = {
        'date_of_ending': forms.DateInput(attrs={'type': 'date'}),
        }
    def __init__(self, *args, **kwargs):
        super(EducationForm, self).__init__(*args, **kwargs)
        self.fields['date_of_ending'].widget.attrs['id'] = 'date-input'
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class LanguageSkillsForm(ModelForm):
    class Meta:
        model = LanguageSkills
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(LanguageSkillsForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class PhotoStudentForm(ModelForm):
    class Meta:
        model = PhotoStudent
        exclude = ('user',)
    def __init__(self, *args, **kwargs):
        super(PhotoStudentForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

class UserEditForm(ModelForm):
    old_password = forms.CharField(required=False,label='Старый пароль')
    password = forms.CharField(required=False,label='Новый пароль')
    def clean_password(self):
        phone = self.cleaned_data.get('password')
        if len(phone)!=0 and len(phone)<7:
            raise forms.ValidationError('Пароль должен состоять из не менее 7 символов')
        return phone
    
    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            

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


class StudentEditForm(ModelForm):
    class Meta:
        model = Student
        fields = ('student_id', 'course', 'speciality', 'phone')

    def __init__(self, *args, **kwargs):
        super(StudentEditForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            