from django.contrib import admin
from .models import UserProfile
from photos.models import Photo
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin


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
    inlines = [PhotoInline,]
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


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    fk_name = 'user'
    fields = ('name', 'birthday', 'gender', 'sex_orientation', 'about')


class CustomUserAdmin(UserAdmin):
    inlines = (UserProfileInline, )

    list_display = (
        'get_name',
        'get_last_login',
        'get_age',
        'get_gender',
        'get_sex_orientation',

    )

    def get_name(self, obj):
        return obj.profile.name

    get_name.admin_order_field = 'name'
    get_name.short_description = 'name'

    def get_age(self, obj):
        return obj.profile.age

    get_age.admin_order_field = 'age'
    get_age.short_description = 'age'

    def get_gender(self, obj):
        return obj.profile.gender

    get_gender.admin_order_field = 'gender'
    get_gender.short_description = 'gender'

    def get_sex_orientation(self, obj):
        return obj.profile.sex_orientation

    get_sex_orientation.admin_order_field = 'sex_orientation'
    get_sex_orientation.short_description = 'sex_orientation'

    def get_last_login(self, obj):
        return obj.last_login

    get_last_login.admin_order_field = 'last_login'
    get_last_login.short_description = 'last_login'


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
