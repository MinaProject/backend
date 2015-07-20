from django.contrib import admin

# Register your models here.
from .models import Story
from.models import UserProfile
admin.site.register(Story)
admin.site.register(UserProfile)