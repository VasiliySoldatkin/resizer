from django.db import models
from django.core.validators import ValidationError
from .storage import OverwriteStorage
from .utils.image_utils import get_image_from_url, get_cleaned_image_name


# TODO: Validate fields (picture, url, parent_picture)
class ImagesModel(models.Model):
    name = models.CharField(max_length=250, blank=True)
    url = models.URLField(blank=True, null=True)
    picture = models.ImageField(verbose_name='picture',
                                height_field='height',
                                width_field='width',
                                upload_to='resizer/%m/%d',
                                storage=OverwriteStorage(),
                                blank=True)
    height = models.PositiveSmallIntegerField(blank=True, null=True, editable=False)
    width = models.PositiveSmallIntegerField(blank=True, null=True, editable=False)
    parent_picture = models.ForeignKey('self',
                                       blank=True,
                                       null=True,
                                       on_delete=models.deletion.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_update = models.DateTimeField(auto_now=True, blank=True)

    def clean(self):
        self.validate_input()
        return super().clean()

    # TODO: Add URL validation (not image files check)
    def validate_input(self):
        if not self.url and not self.picture:
            raise ValidationError(message='Please, upload the image by URL or File')
        if self.url and self.picture:
            raise ValidationError(message='Please, choose only one of upload options')

    def save(self, *args, **kwargs):
        if self.url and not self.picture.name:
            file_name, fp = get_image_from_url(self.url)
            self.picture.save(file_name, fp)
            self.name = get_cleaned_image_name(self.picture.name)
        if not self.name:
            self.name = self.picture.name

        super().save(*args, **kwargs)

# Create your models here.
