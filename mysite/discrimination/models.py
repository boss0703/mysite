from django.db import models


class ImageFile(models.Model):
    inputFile = models.FileField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
