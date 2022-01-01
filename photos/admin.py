from django.contrib import admin
from .models import Photo
from django.utils.html import mark_safe


class PhotoAdmin(admin.ModelAdmin):
    fields = ('image', 'image_tag', 'description', 'user')
    list_display = ('image_tag', 'description', 'user')
    readonly_fields = ('image_tag',)

    def image_tag(self, obj):
        return mark_safe('<img src="{}" / width="120", height="150">'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


admin.site.register(Photo, PhotoAdmin)
