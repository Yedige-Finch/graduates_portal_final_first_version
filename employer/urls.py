from django.urls import path

from . import views

urlpatterns = [
	path('', views.employer_home, name='employer_home'),
	path('edit_employer/', views.edit_employer, name='edit_employer'),
	path('edit_employer_user/', views.edit_employer_user, name='edit_employer_user'),
	path('edit_employer_profile/', views.edit_employer_profile, name='edit_employer_profile'),
	path('edit_employer/<saved>', views.edited_employer, name='edited_employer'),
	path('company/', views.company, name='company'),
	path('company/<saved>', views.edited_company, name='edited_company'),
	path('company_get/', views.company_get, name='company_get'),
	path('candidates/', views.candidates, name='candidates'),
	path('invite_student/', views.invite_student, name='invite_student'),
	path('reject_student/', views.reject_student, name='reject_student'),
	path('vacancy/', views.vacancy, name='vacancy'),
	path('vacancy/<int:vac_id>', views.vacancy_edit, name='vacancy_edit'),
	path('vacancy/<saved>', views.edited_vacancy, name='edited_vacancy'),
	path('vacancy_get/', views.vacancy_get, name='vacancy_get'),
	path('vacancy_get/<int:vac_id>', views.vacancy_detail_employer, name='vacancy_detail_employer'),
	path('vacancy_get/<int:vac_id>/<int:resp_id>', views.vacancy_detail_employer, name='vacancy_detail_employer'),
	path('resume_employer/', views.resume_employer, name='resume_employer'),
	path('resume_employer/<str:user>/<int:resp_id>', views.get_resume_student, name='get_resume_student'),
	path('vacancy_get/remove_vacancy/<int:vac_id>', views.remove_vacancy, name='remove_vacancy'),
 ]