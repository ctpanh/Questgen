from django.db import models

# Create your models here.

class QuestionModel(models.Model):
    file = models.FileField(blank=True, null=True, upload_to="store")
    text = models.TextField(default="")
    easy = models.PositiveIntegerField(default=1)
    medium = models.PositiveIntegerField(default=1)
    hard = models.PositiveIntegerField(default=1)
    quest_type = models.TextField(default="boolean")
    def __str__(self):
        return self.file.name
