# -*- coding: utf-8 -*-
from django.contrib import admin
from ekg.models import EKG


class EKGAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'frequency', 'pulse_generated', 'created_date',)
    search_fields = ('title', 'pulse')
    list_filter = ('created_date',)
admin.site.register(EKG, EKGAdmin)
