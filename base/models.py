from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Creates the book database fields


class BookDatabase(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    grade_level = models.CharField(max_length=10, null=True, blank=True)
    lexile_score = models.IntegerField
    inventory = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    modified_by = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'grade_level': self.grade_level,
            'inventory': self.inventory,
            'updated': self.updated,
            'created': self.created
        }


class LexileData(models.Model):
    ISBN = models.IntegerField()
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    lexile_score = models.IntegerField()
