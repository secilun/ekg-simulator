# -*- coding: utf-8 -*-
from django.contrib import admin
from pulse.models import Pulse


class PulseAdmin(admin.ModelAdmin):
    list_display = ('id', 'ekg', 'pulse1', 'ptype1', 'pulse2', 'ptype2', 'pulse3', 'ptype3', 'created_date',)
    list_filter = ('created_date', 'ekg',)
admin.site.register(Pulse, PulseAdmin)
