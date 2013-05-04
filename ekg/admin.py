# -*- coding: utf-8 -*-
from django.contrib import admin
from ekg.models import EKG, SelectedEKG


class EKGAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'pulse_generated', 'created_date',)
    search_fields = ('title', 'pulse')
    list_filter = ('created_date',)
admin.site.register(EKG, EKGAdmin)


class SelectedEKGAdmin(admin.ModelAdmin):
    list_display = ('id', 'ekg', 'created_date',)
    list_filter = ('created_date',)
admin.site.register(SelectedEKG, SelectedEKGAdmin)
