from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_out
from django.contrib import messages


class UserProfile(models.Model):
    ALBERTA = 1
    BRITISH_COLUMBA = 2
    MANITOBA = 3
    NEW_BRUNSWICK = 4
    NEWFOUNDLAND = 5
    NORTHWEST_TERRITORIES = 6
    NOVA_SCOTIA = 7
    NUNAVUT = 8
    ONTARIO = 9
    PEI = 10
    QUEBEC = 11
    SASKATCHEWAN = 12
    YUKON = 13

    PROVINCES = (
        (0, 'Choose your province'),
        (ALBERTA, 'Alberta'),
        (BRITISH_COLUMBA, 'British Columbia'),
        (MANITOBA, 'Manitoba'),
        (NEW_BRUNSWICK, 'New Brunswick'),
        (NEWFOUNDLAND, 'Newfoundland & Labraador'),
        (NORTHWEST_TERRITORIES, 'Northwest Territories'),
        (NOVA_SCOTIA, 'Nova Scotia'),
        (NUNAVUT, 'Nunavut'),
        (ONTARIO, 'Ontario'),
        (PEI, 'Prince Edward Island'),
        (QUEBEC, 'Quebec'),
        (SASKATCHEWAN, 'Saskatchewan'),
        (YUKON, 'Yukon')
    )
    user = models.ForeignKey(User)
    company = models.CharField(blank=True, null=True, max_length=100)
    address = models.CharField(max_length=150)
    city = models.CharField(max_length=40)
    province = models.IntegerField(choices=PROVINCES, default=9)
    postal_code = models.CharField(max_length=7)
    phone = models.CharField(max_length=40, null=True, blank=True)
    website = models.URLField(null=True, blank=True)
    private = models.BooleanField('Please make my address private.', default=False)

    def __unicode__(self):
        return self.user.username

def logout_notifier(sender, request, user, **kwargs):
    messages.success(request, 'You have been logged out.')
user_logged_out.connect(logout_notifier)