from django.urls import path

from . import views

urlpatterns = [
    path('get_answers/', views.get_answers, name='get_answers'),
    path('feedback/', views.feedback, name='feedback'),
    path('feedback/<saved>', views.feedback_saved, name='feedback_saved'),
    path('software_requirements', views.software_requirements, name='software_requirements'),
    path('new/', views.new, name='new'),
    path('new/<int:article_id>', views.news, name='news'),
    ]