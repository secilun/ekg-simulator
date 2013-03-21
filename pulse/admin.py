# -*- coding: utf-8 -*-
from django.contrib import admin
from pulse.models import Pulse


class PulseAdmin(admin.ModelAdmin):
    list_display = ('id', 'ekg', 'pulse', 'created_date',)
    list_filter = ('created_date', 'ekg',)
admin.site.register(Pulse, PulseAdmin)
