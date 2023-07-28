from django.contrib import admin

from .models import BannerImage, Consert, Event


admin.site.register(BannerImage)

@admin.register(Consert)
class _Consert(admin.ModelAdmin):
    list_display = ['name', 'image', 'date', 'language']

@admin.register(Event)
class _Event(admin.ModelAdmin):
    list_display = ['name', 'image', 'date', 'language']