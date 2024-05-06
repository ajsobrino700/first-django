from django.contrib import admin
from polls.domain.choice import Choice
from polls.domain.question import Question
# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)