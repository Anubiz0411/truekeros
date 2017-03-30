from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Album(models.Model):
    owner = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __unicode__(self,):
        return self.title


class AlbumImage(models.Model):
    album = models.ForeignKey(Album, related_name='images')
    image = models.ImageField(upload_to='albums/images/')

    def __unicode__(self,):
        return str(self.image)
