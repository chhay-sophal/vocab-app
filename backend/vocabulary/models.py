from django.db import models

# Create your models here.
class Word(models.Model):
    term = models.CharField(max_length=100, unique=True)
    definition = models.TextField()
    part_of_speech = models.CharField(max_length=50, blank=True, null=True)
    example_sentence = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.term