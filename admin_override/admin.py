from django.contrib import admin
from .models import Advice,Answers,Feedback,Article
# Register your models here.
class AdviceAdmin(admin.ModelAdmin):
    list_display= ('Advice','adv_id','photo', 'render')
    
class AnswersAdmin(admin.ModelAdmin):
    list_display= ('answer_help_type','answer_question','answer', 'render')


class FeedbackAdmin(admin.ModelAdmin):
    list_display= ('topic','content','sent_name', 'e_mail')

class ArticleAdmin(admin.ModelAdmin):
    list_display= ('Author','about_author','Theme', 'Article')

admin.site.register(Advice, AdviceAdmin)  
admin.site.register(Answers, AnswersAdmin)
admin.site.register(Feedback, FeedbackAdmin)  
admin.site.register(Article, ArticleAdmin)

