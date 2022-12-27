from django.db import models

# Create your models here.

#Creates the book database fields
class BookDatabase(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    lexile_score = models.CharField(max_length=5)
    inventory = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    #orders the database by ascending title then author
    class Meta:
        ordering = ['title', 'author']

    def __str__(self):
        return self.title
        
