from django.contrib import admin

from .models import Album, AlbumImage


class AlbumImageInline(admin.TabularInline):
    model = AlbumImage
    extra = 3

class AlbumAdmin(admin.ModelAdmin):
    inlines = [ AlbumImageInline, ]


admin.site.register(Album)
admin.site.register(AlbumImage)
