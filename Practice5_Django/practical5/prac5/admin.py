from django.contrib import admin
from .models import checkdb

# Register your models here.
class myAdmin(admin.ModelAdmin):
  list_display = ("email",)


admin.site.register(checkdb, myAdmin)