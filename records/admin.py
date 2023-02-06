from django.contrib import admin

from records.models import Record


@admin.register(Record)
class RecordAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'uuid',
        'created',
        'body',
        'active'
    )

    fieldsets = (
            (None, {'fields': ('body', 'active',)}),
    )
