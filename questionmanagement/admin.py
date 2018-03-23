from django.contrib import admin
from .models import Questions, QuestionType, QuestionChoices, Complexity


admin.site.register(Questions)
admin.site.register(QuestionType)
admin.site.register(QuestionChoices)
admin.site.register(Complexity)