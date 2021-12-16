from django.contrib import admin
from .models import UserProfile
from photos.models import Photo
from django.utils.html import mark_safe


class PhotoInline(admin.TabularInline):
    model = Photo
    fields = ('image', 'image_tag', 'description', 'user')
    list_display = ('image_tag', 'description', 'user')
    readonly_fields = ('image_tag',)
    
    def image_tag(self, obj):
        return mark_safe('<img src="{}" / width="150", height="150">'.format(obj.image.url))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True


class UserProfileAdmin(admin.ModelAdmin):
    inlines =[PhotoInline,]
    fields = ['user',
              'name',
              'birthday',
              'gender',
              'sex_orientation',
              'about'
              ]
    list_display = ['user',
                    'name',
                    'age',
                    'birthday',
                    'gender',
                    'sex_orientation'
                    ]



admin.site.register(UserProfile, UserProfileAdmin)
