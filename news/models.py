from django.db import models
import datetime

# Create your models here.
class Headline(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    hotness_label = models.CharField(max_length=200, blank=True)
    utility_label = models.CharField(max_length=200, blank=True)
    image_link = models.CharField(max_length=200, blank=True)
    youtube_link = models.CharField(max_length=200, blank=True)
    vimeo_link = models.CharField(max_length=200, blank=True)
    video_link = models.CharField(max_length=200, blank=True)
    itunes_link = models.CharField(max_length=200, blank=True)
    appstore_link = models.CharField(max_length=200, blank=True)
    play_link = models.CharField(max_length=200, blank=True)
    windows_link = models.CharField(max_length=200, blank=True)
    steam_link = models.CharField(max_length=200, blank=True)
    indie_link = models.CharField(max_length=200, blank=True)
    company_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200)
    source2_link = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.subject

    def published_today(self):
        return self.publication_date.date() == datetime.date.today()
    published_today.boolean = True
    published_today.short_description = 'Asked today?'