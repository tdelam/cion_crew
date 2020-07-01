from django.db import models
from django.contrib.auth.models import User

from crew import CREWS


class Skills(models.Model):
    available_as = models.TextField(null=True, blank=True)
    weblink_1 = models.URLField('Weblink 1', null=True, blank=True)
    weblink_1_description = models.CharField('Description', null=True, blank=True, max_length=200)
    weblink_2 = models.URLField('Weblink 2', null=True, blank=True)
    weblink_2_description = models.CharField('Description', null=True, blank=True, max_length=200)
    weblink_3 = models.URLField('Weblink 3', null=True, blank=True)
    weblink_3_description = models.CharField('Description', null=True, blank=True, max_length=200)
    resume = models.FileField('Upload a Resume', upload_to='uploads/', null=True, blank=True)
    dgc = models.BooleanField('DGC Directors Guild of Canada', default=False)
    iatse = models.BooleanField('IATSE', default=False)
    actra = models.BooleanField('ACTRA - Alliance of Cinema, Television and Radio Artists', default=False)
    wgc = models.BooleanField('WGC Writers Guild of Canada', default=False)
    cpma = models.BooleanField('CMPA Member', default=False)
    resident = models.BooleanField('I am a Northern Ontario resident', default=False)
    other = models.CharField('Other', null=True, blank=True, max_length=150)
    user = models.ForeignKey(User, null=True, blank=True)
    last_updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    class Meta:
        verbose_name_plural = "Skills"


    def __unicode__(self):
        return self.user.username

    @models.permalink
    def get_absolute_url(self):
        return ('view_skills', [self.user.pk])

class CreditOptions(models.Model):
    year = models.IntegerField(max_length=4, help_text='e.g. 1995', null=True, blank=True)
    project_name = models.CharField(max_length=150, null=True, blank=True)
    imdb_credited = models.BooleanField('IMDB Credited', default=False)
    crew_position = models.IntegerField(choices=CREWS, default=0, null=True)
    user = models.ForeignKey(User, null=True, blank=True)

    def __unicode__(self):
        return self.user.username

    class Meta:
        verbose_name_plural = "Credit Options"