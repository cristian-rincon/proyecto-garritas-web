from django.contrib import admin

from .models import Suite

# Register your models here.


@admin.register(Suite)
class SuitesAdmin(admin.ModelAdmin):
    list_display = ("name", "description", "price", "available")
    list_filter = ("available",)
    search_fields = ("name", "description")
    ordering = ("name",)
    fieldsets = (
        (None, {"fields": ("name", "description", "price", "available", "photo")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("name", "description", "price", "available", "photo"),
            },
        ),
    )
    readonly_fields = ("created", "updated")
