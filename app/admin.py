from django.contrib import admin
from app.models import Question, Answer, Tag, Like, Profile


admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Tag)
admin.site.register(Like)
admin.site.register(Profile)

