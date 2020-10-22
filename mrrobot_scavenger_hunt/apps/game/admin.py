from django.contrib import admin

from mrrobot_scavenger_hunt.apps.game.models import *

class StepInline(admin.TabularInline):
    model = Step

class PathAdmin(admin.ModelAdmin):
    inlines = [
        StepInline,
    ]

class GameStepInline(admin.TabularInline):
    model = GameStep

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameStepInline,
    ]

admin.site.register(Attack)
admin.site.register(Puzzle)
admin.site.register(Station)
admin.site.register(Path, PathAdmin)
admin.site.register(Game, GameAdmin)
