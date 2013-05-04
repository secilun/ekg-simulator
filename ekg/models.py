# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _


# Create your models here.
class EKG(models.Model):
    title = models.CharField(_('title'), max_length=100)

    pulse1 = models.TextField(_('height 1'))
    ptype1 = models.TextField(_('pytpe 1'))

    pulse2 = models.TextField(_('height 2'))
    ptype2 = models.TextField(_('pytpe 2'))

    pulse3 = models.TextField(_('height 3'))
    ptype3 = models.TextField(_('pytpe 3'))

    pulse_generated = models.BooleanField(editable=False)
    last_sent = models.IntegerField(default=0, editable=False)

    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.title)

    def get_absolute_url(self):
        return "/ekg/%s/plain/" % (self.id)

    def save(self, *args, **kwargs):
        if not self.id:
            pass
        super(EKG, self).save(*args, **kwargs)
 
    class Meta:
        verbose_name = _('EKG')
        verbose_name_plural = _('EKGs')


class SelectedEKG(models.Model):
    ekg = models.ForeignKey(EKG, verbose_name=_('ekg'))
    created_date = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "%s" % (self.ekg.title)

 
    class Meta:
        verbose_name = _('Selected EKG')
        verbose_name_plural = _('Selected EKGs')
