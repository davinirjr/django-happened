from django.db import models


class Event(models.Model):
    group = models.CharField(max_length=30, blank=True)
    start = models.DateTimeField()
    start_resolution = models.IntegerField(default=0)
    end = models.DateTimeField(null=True, blank=True)
    end_resolution = models.IntegerField(default=0)
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return self.title


class Url(models.Model):
    event = models.ForeignKey(Event, related_name='urls')
    order = models.IntegerField(default=1)
    url = models.URLField()

    def __unicode__(self):
        return self.url
