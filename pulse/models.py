# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ekg.models import EKG


# Create your models here.
class Pulse(models.Model):
    ekg = models.ForeignKey(EKG, related_name='ekg', verbose_name=_('ekg'))

    pulse1 = models.FloatField(_('pulse 1'))
    ptype1 = models.CharField(_('type 1'), max_length=200)

    pulse2 = models.FloatField(_('pulse 2'))
    ptype2 = models.CharField(_('type 2'), max_length=200)

    pulse3 = models.FloatField(_('pulse 3'))
    ptype3 = models.CharField(_('type 3'), max_length=200)

    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.id)

    class Meta:
        verbose_name = _('Pulse')
        verbose_name_plural = _('Pulses')



