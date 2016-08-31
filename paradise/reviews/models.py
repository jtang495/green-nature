from __future__ import unicode_literals

from django.db import models
import numpy as np

def upload_location(obj, filename):
    return "%s/%s" %(obj.id, filename)
    
class Wine(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to = upload_location, null=True, blank=True, width_field="width_field", height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    def average_rating(self):
        all_ratings = map(lambda x: x.rating, self.review_set.all())
        return np.mean(all_ratings)

    def __unicode__(self):
        return self.name

class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField('date published')
    image1 = models.ImageField(upload_to = upload_location, null=True, blank=True) 
    image2 = models.ImageField(upload_to = upload_location, null=True, blank=True) 
    image3 = models.ImageField(upload_to = upload_location, null=True, blank=True) 



class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
    )
    wine = models.ForeignKey(Wine)
    pub_date = models.DateTimeField('date published')
    user_name = models.CharField(max_length=100)
    comment = models.CharField(max_length=200)
    rating = models.IntegerField(choices=RATING_CHOICES)
