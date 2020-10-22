from django.contrib import admin

from mrrobot_scavenger_hunt.apps.game.models import *

class StepInline(admin.TabularInline):
    model = Step

class PathAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]

def start_mission(modeladmin, request, queryset):
    Game.objects.all().update(on_mission=True)
start_mission.short_description = "Start Mission"

def end_mission(modeladmin, request, queryset):
    Game.objects.all().update(on_mission=False)
end_mission.short_description = "End Mission"

class GameStepInline(admin.TabularInline):
    model = GameStep

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameStepInline,
    ]
    list_display = ('user', 'score', 'mode', 'status', 'on_mission' )
    actions = [start_mission, end_mission]
    

admin.site.register(Attack)
admin.site.register(Puzzle)
admin.site.register(Station)
admin.site.register(Path, PathAdmin)
admin.site.register(Game, GameAdmin)
