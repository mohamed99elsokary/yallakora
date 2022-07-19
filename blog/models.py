from django.db import models
from ckeditor.fields import RichTextField
from core.models import TimeStampedModel


class Post(TimeStampedModel):

    title = models.CharField(max_length=255)
    content = RichTextField(config_name="awesome_ckeditor")
    image = models.ImageField(upload_to="media/")

    def __str__(self) -> str:
        return self.title
