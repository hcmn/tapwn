from django.db import models

# Create your models here.
class Headline(models.Model):
    publication_date = models.DateTimeField(auto_now_add=True)
    subject = models.CharField(max_length=200)
    description = models.TextField()
    image_link = models.CharField(max_length=200)
    source_link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.subject