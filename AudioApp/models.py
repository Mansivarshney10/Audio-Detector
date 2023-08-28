from django.db import models

# Create your models here.
class AudioFile(models.Model):
    file = models.FileField(upload_to='audio_files/')
    upload_date = models.DateTimeField(auto_now_add=True)
    file_size = models.PositiveIntegerField()
    file_extension = models.CharField(max_length=5)

    def __str__(self):
        return self.file.name