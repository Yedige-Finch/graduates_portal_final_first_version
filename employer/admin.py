from django.contrib import admin
from .models import Company,Vacancy,Respond,FavoriteVacancy,UndesirableVacancy,FavoriteCompany,UndesirableCompany
# Register your models here.
admin.site.register(Company)
admin.site.register(Vacancy)
admin.site.register(Respond)

admin.site.register(FavoriteVacancy)
admin.site.register(UndesirableVacancy)
admin.site.register(FavoriteCompany)
admin.site.register(UndesirableCompany)