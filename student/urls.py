from django.urls import path

from . import views

urlpatterns = [
    path('', views.student_home, name='student_home'),
    
    path('resume/', views.resume, name='resume'),
    
    path('pers_inform_save/', views.pers_inform_save, name='pers_inform_save'),
    path('contact_information_save/', views.contact_information_save, name='contact_information_save'),
    path('desired_position_save/', views.desired_position_save, name='desired_position_save'),
    path('experience_save/', views.experience_save, name='experience_save'),
    path('about_student_save/', views.about_student_save, name='about_student_save'),
    path('education_save/', views.education_save, name='education_save'),
    path('language_skills_save/', views.language_skills_save, name='language_skills_save'),
    path('resume_saved/<saved>', views.resume_saved, name='resume_saved'),
    path('photo_student/', views.photo_student, name='photo_student'),
    path('photo_student_save/', views.photo_student_save, name='photo_student_save'),
    
    path('get_resume_student/', views.get_resume_student, name='get_resume_student'),
    path('pers_inform/', views.pers_inform, name='pers_inform'),
    path('contact_information/', views.contact_information, name='contact_information'),
    path('desired_position/', views.desired_position, name='desired_position'),
    path('experience/', views.experience, name='experience'),
    path('about_student/', views.about_student, name='about_student'),
    path('education/', views.education, name='education'),
    path('language_skills/', views.language_skills, name='language_skills'),

    path('edit_student/', views.edit_student, name='edit_student'),
    path('edit_student_user/', views.edit_student_user, name='edit_student_user'),
    path('edit_student_profile/', views.edit_student_profile, name='edit_student_profile'),
    path('edit_student/<saved>', views.edited_student, name='edited_student'),

    path('<int:vac_id>', views.vacancy_detail_get, name='vacancy_detail_get'),
    path('<str:company_name>', views.company_detail_get, name='company_detail_get'),
    
    path('student_respond/', views.student_respond, name='student_respond'),
    path('add_to_favorite_vacancy/', views.add_to_favorite_vacancy, name='add_to_favorite_vacancy'),
    path('add_to_undesirable_vacancy/', views.add_to_undesirable_vacancy, name='add_to_undesirable_vacancy'),
    path('remove_from_favorite_vacancy/', views.remove_from_favorite_vacancy, name='remove_from_favorite_vacancy'),
    path('remove_from_undesirable_vacancy/', views.remove_from_undesirable_vacancy, name='remove_from_undesirable_vacancy'),
    path('responses_and_invitations/', views.responses_and_invitations, name='responses_and_invitations'),
    path('favorite_vacancies/', views.favorite_vacancies, name='favorite_vacancies'),
    path('undesirable_vacancies/', views.undesirable_vacancies, name='undesirable_vacancies'),
    path('some_view/', views.some_view, name='some_view'),
    path('recommendation_all/', views.recommendation_all, name='recommendation_all'),
    path('vacancy_of_the_day_all/', views.vacancy_of_the_day_all, name='vacancy_of_the_day_all'),
    
]