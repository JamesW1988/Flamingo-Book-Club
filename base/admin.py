from django.contrib import admin

# Register your models here.

from .models import BookDatabase
from .models import LexileData

admin.site.register(BookDatabase)
admin.site.register(LexileData)
