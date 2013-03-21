# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from ekg.models import EKG


# Create your models here.
class Pulse(models.Model):
    ekg = models.ForeignKey(EKG, related_name='ekg', verbose_name=_('ekg'))
    pulse = models.IntegerField(_('pulse'))

    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.pulse)

    class Meta:
        verbose_name = _('Pulse')
        verbose_name_plural = _('Pulses')



