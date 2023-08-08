from django.db import models

# Create your models here.

class FileModel(models.Model):
    # name = models.CharField(blank=False, max_length=100)
    # types = models.IntegerField(default=0)
    file = models.FileField(blank=True, null=True, upload_to="store")
    text = models.TextField(default="")
    easy = models.IntegerField(default=1)
    medium = models.IntegerField(default=1)
    hard = models.IntegerField(default=1)
    type = models.IntegerField(default=0)
    def __str__(self):
        return self.file.name
