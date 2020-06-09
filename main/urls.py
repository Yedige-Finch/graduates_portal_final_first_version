from django.urls import path

from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('get_vacancy_main/', views.get_vacancy_main, name='get_vacancy_main'),
    path('get_company_main/', views.get_company_main, name='get_company_main'),
    path('get_vacancy_main/<int:vac_id>', views.vacancy_detail_get, name='vacancy_detail_get'),
    path('get_company_main/<str:company_name>', views.company_detail_get, name='company_detail_get'),
    path('search/', views.search_vacancy, name='search_vacancy'),
 ]