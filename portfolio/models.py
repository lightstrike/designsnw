from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from model_utils.models import TimeStampedModel, StatusModel
from model_utils import Choices
from autoslug import AutoSlugField


@python_2_unicode_compatible
class Portfolio(TimeStampedModel, StatusModel):
    """
    Portfolio model stores information about completed
    projects
    """
    STATUS = Choices('draft', 'published')
    PROPERTY_CHOICES = Choices('residential', 'commericial', 'community')

    title = models.CharField(max_length=128)
    slug = AutoSlugField(populate_from='title')
    property_type = models.CharField(choices=PROPERTY_CHOICES,
                                     default=PROPERTY_CHOICES.residential,
                                     max_length=64)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    def featured_image(self):
        return self.images.filter(featured=True).first()


@python_2_unicode_compatible
class PortfolioImage(TimeStampedModel):
    portfolio = models.ForeignKey(Portfolio, related_name='images')
    title = models.CharField(max_length=128)
    file_path = models.ImageField(upload_to='portfolio',
                                  blank=True, null=True)
    front_page = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    order = models.IntegerField(default=0)

    def __str__(self):
        return "{}: {}".format(self.portfolio.title,
                               self.title)
