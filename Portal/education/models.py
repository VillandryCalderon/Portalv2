from django.db import models
from django.utils.translation import ugettext as _


class Institution(models.Model):
    name = models.CharField(_('University or institution'), max_length=64)

    class Meta:
        verbose_name = _('University or institution')
        verbose_name_plural = _('Universities or institutions')
        ordering = ('name',)

    def __str__(self):
        return self.name


class Certification(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name = _('Certification')
        verbose_name_plural = _('Certifications')
        ordering = ('name',)

    def __str__(self):
        return self.name
