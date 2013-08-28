from django.db import models
import datetime

# Create your models here.
class Headline(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    schedule_content = models.DateTimeField()
    subject = models.CharField(max_length=200)
    description = models.TextField()
    hotness_label = models.CharField(max_length=200, blank=True)
    utility_label = models.CharField(max_length=200, blank=True)
    functional_label = models.CharField(max_length=200, blank=True)
    image_link = models.ImageField(upload_to='content', blank=True)
    image2_link = models.ImageField(upload_to='content', blank=True)
    youtube_link = models.CharField(max_length=200, blank=True)
    vimeo_link = models.CharField(max_length=200, blank=True)
    video_link = models.CharField(max_length=200, blank=True)
    itunes_link = models.CharField(max_length=200, blank=True)
    appstore_link = models.CharField(max_length=200, blank=True)
    play_link = models.CharField(max_length=200, blank=True)
    windows_link = models.CharField(max_length=200, blank=True)
    sony_link = models.CharField(max_length=200, blank=True)
    nintendo_link = models.CharField(max_length=200, blank=True)
    steam_link = models.CharField(max_length=200, blank=True)
    ouya_link = models.CharField(max_length=200, blank=True)
    indie_link = models.CharField(max_length=200, blank=True)
    facebook_link = models.CharField(max_length=200, blank=True)
    pinterest_link = models.CharField(max_length=200, blank=True)
    twitter_link = models.CharField(max_length=200, blank=True)
    company_link = models.CharField(max_length=200, blank=True)
    amazon_link = models.CharField(max_length=200, blank=True)
    affiliate_link = models.CharField(max_length=200, blank=True)
    source_link = models.CharField(max_length=200)
    source2_link = models.CharField(max_length=200, blank=True)
    author_name = models.CharField(max_length=200, blank=True)
    author_link = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.subject

    def published_today(self):
        return self.publication_date.date() == datetime.date.today()
    published_today.boolean = True
    published_today.short_description = 'Asked today?'