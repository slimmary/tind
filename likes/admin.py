from django.contrib import admin
from .models import Like


class LikeAdmin(admin.ModelAdmin):
    fields = ['sender',
              'recipient',
              ]
    list_display = ['sender',
                    'recipient',
                    ]


admin.site.register(Like, LikeAdmin)

