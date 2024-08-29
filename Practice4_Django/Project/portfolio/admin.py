from django.contrib import admin
from .models import mydata

# class dataMembers(admin.ModelAdmin):
#     list_display = ['fname', 'lname','phone']

admin.site.register(mydata)