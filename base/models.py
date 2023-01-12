from django.db import models

# Create your models here.

# Creates the book database fields


class BookDatabase(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    grade_level = models.CharField(max_length=10, null=True, blank=True)
    condition = models.CharField(max_length=10, null=True, blank=True, choices=(
        ('Good', 'Good'),
        ('Fair', 'Fair'),
        ('Poor', 'Poor'),
    ))
    inventory = models.IntegerField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    # orders the database by ascending title then author
    class Meta:
        ordering = ['title', 'author']

    def __str__(self):
        return self.title

    def as_dict(self):
        return {
            'title': self.title,
            'author': self.author,
            'description': self.description,
            'grade_level': self.grade_level,
            'condition': self.condition,
            'inventory': self.inventory,
            'updated': self.updated,
            'created': self.created
        }
