# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class EKG(models.Model):
    title = models.CharField(_('title'), max_length=100)
    frequency = models.IntegerField(_('frequency'))
    pulse = models.CharField(_('pulse'), max_length=250)
    pulse_generated = models.BooleanField(editable=False)
    last_sent = models.IntegerField(default=0)

    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.id)

    def get_absolute_url(self):
        return "/ekg/%s/plain/" % (self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            pass
        super(EKG, self).save(*args, **kwargs)
 
    class Meta:
        verbose_name = _('EKG')
        verbose_name_plural = _('EKGs')
