from django.db import models

CHOICES = (('morning', 'Morning'), ('afternoon', 'Afternoon'))
class Book(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField(blank=True, null=True)
    content = models.TextField(default='some content')
    author = models.CharField(max_length=10)

    def __str__(self):
        return self.title
