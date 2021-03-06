from django.contrib import admin

from teams.models import Team


@admin.register(Team)
class KitAdmin(admin.ModelAdmin):
    list_display = ["name", "short_name", "fpl_id", "understat_id"]
    ordering = ["name"]
