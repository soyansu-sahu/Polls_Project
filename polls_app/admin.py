from django.contrib import admin
from .models import Poll, Choice, UserResponse


# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice)
admin.site.register(UserResponse)
