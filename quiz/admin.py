from django.contrib import admin

from quiz.models import Question, Quiz


# updates to the admin since the default django many-to-many relationship interface is not as nice
class QuestionsInline(admin.TabularInline):
    model = Quiz.questions.through
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'date_added')
    search_fields = ('name', 'description', 'content')
    exclude = ['questions']
    inlines = [QuestionsInline]


admin.site.register(Quiz, QuizAdmin)


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('pk', 'text', 'answer')
    search_fields = ('text',)


admin.site.register(Question, QuestionAdmin)
