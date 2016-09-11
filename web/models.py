from __future__ import unicode_literals

from django.db import models
from tinymce import models as tinymce_models
import numpy as np

def upload_location(obj, filename):
    return "%s/%s" %(obj.id, filename)
    
class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default="")
    image = models.ImageField(upload_to = upload_location, null=True, blank=True)
    link1_title = models.CharField(max_length=100)
    link1_link = models.CharField(max_length=200, help_text="Make sure the link starts with 'https://'")
    link2_title = models.CharField(max_length=200)
    link2_link = models.CharField(max_length=200, help_text="Make sure the link starts with 'https://'")
#    link2_link = models.CharField(max_length=200, help_text="Make sure the link starts with 'https://'")
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = tinymce_models.HTMLField()
    pub_date = models.DateTimeField('date published')
    image1 = models.ImageField(upload_to = upload_location, null=True, blank=True) 
    image2 = models.ImageField(upload_to = upload_location, null=True, blank=True) 
    image3 = models.ImageField(upload_to = upload_location, null=True, blank=True) 
    image4 = models.ImageField(upload_to = upload_location, null=True, blank=True) 


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    product = models.ForeignKey(Product)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
