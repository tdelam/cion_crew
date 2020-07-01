from django.db import models


class SearchTerm(models.Model):
    q = models.CharField(max_length=50)
    search_date = models.DateTimeField(auto_now=True)
    ip_address = models.IPAddressField()
    
    def __unicode__(self):
        return self.q