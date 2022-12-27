from django.forms import ModelForm
from .models import BookDatabase


class DatabaseForm(ModelForm):
    class Meta:
        model = BookDatabase
        fields = '__all__'