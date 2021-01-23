from django.core.validators import FileExtensionValidator
from django.db import models


class ImageFile(models.Model):
    titlefield = models.CharField(max_length=200, null = True)
    filefield = models.FileField(
        upload_to='images/',
        verbose_name='attached file',
        validators=[FileExtensionValidator(['jpg', ])],
        null=True
    )
#    uploaded_at = models.DateTimeField(auto_now_add=True)
