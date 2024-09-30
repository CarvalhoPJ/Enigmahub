from django.db import models

# Create your models here.

class Enigma(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    tips = models.TextField()
    correct_answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    resolved = models.BooleanField(default=False)
    answers = models.IntegerField(default=0)

    def __str__(self):
        return self.title

