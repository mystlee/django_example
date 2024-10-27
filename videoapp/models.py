from django.db import models

# Create your models here.
class Video(models.Model):
    original_video = models.FileField(upload_to='videos/original/')
    processed_video = models.FileField(upload_to='videos/processed/', blank=True, null=True)

    def __str__(self):
        return self.original_video.name

