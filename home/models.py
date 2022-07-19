from django.db import models

# Create your models here.
class Image(models.Model):
    # relations
    image = models.ImageField(
        upload_to="media/", height_field=None, width_field=None, max_length=None
    )
    # fields

    def __str__(self):
        return str(self.id)
