from django.contrib.auth.models import User as DjangoUser
from django.db import models


class ClientSite(models.Model):
    """Client site allowed to authenticate against this SSO service."""
    name = models.CharField(max_length=255, unique=True, null=False)
    domain = models.CharField(
        max_length=255, unique=True, null=False,
        help_text='Domain name incoming service requests are matched against.')
    match_priority = models.IntegerField(default=0)

    # users who have given this site access to their user account.
    users = models.ManyToManyField(DjangoUser, null=True, blank=True,
                                   related_name='sites')

    class Meta:
        ordering = ('-match_priority',)
        verbose_name = 'Client Site'

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.domain)
