from django.contrib import admin
from .models import PersonalInformation,ContactInformation,DesiredPosition,Experience,AboutStudent,Education,LanguageSkills,PhotoStudent
# Register your models here.
admin.site.register(PersonalInformation)
admin.site.register(ContactInformation)
admin.site.register(DesiredPosition)
admin.site.register(Experience)
admin.site.register(AboutStudent)
admin.site.register(Education)
admin.site.register(LanguageSkills)
admin.site.register(PhotoStudent)
