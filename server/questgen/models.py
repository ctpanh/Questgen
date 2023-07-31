from django.db import models

# Create your models here.

class FileModel(models.Model):
    # name = models.CharField(blank=False, max_length=100)
    # types = models.IntegerField(default=0)
    file = models.FileField(blank=True, null=True, upload_to="store")
    text = models.TextField(default="")
    def __str__(self):
        return self.file.name
