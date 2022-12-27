from django.contrib import admin

# Register your models here.

from .models import BookDatabase

admin.site.register(BookDatabase)