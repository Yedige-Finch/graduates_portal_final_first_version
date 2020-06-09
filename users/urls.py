from django.urls import path

from . import views

urlpatterns = [
	path('login',views.login,name = 'login'),
	path('register_student',views.registration_student,name = 'registration_student'),
	path('register_employer',views.registration_employer,name = 'registration_employer'),
	path('logout',views.logout,name = 'logout'),
]