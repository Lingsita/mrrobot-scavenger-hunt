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
    save_log(request.user, f'Start Mission')
start_mission.short_description = "Start Mission"


def end_mission(modeladmin, request, queryset):
    Game.objects.all().update(on_mission=False)
    save_log(request.user, f'End mission')
end_mission.short_description = "End Mission"


def save_log(user, message):
    try:
        log = Log.objects.create(user=user, message=message)
        log.save()
    except Exception as e:
        print(e)


def approve_attack(modeladmin, request, queryset):
    for game in queryset:
        if game.status is not Game.FINISHED:
            game_step = game.current_step
            if game_step.is_puzzle_solved:
                game_step.is_attack_approved = True
                game_step.save()
                game.score = game.score + 1
                game.mode = Game.CYPHER
                game.save()
                save_log(request.user, f'Attack approved for user_id: {game.user.id}')
approve_attack.short_description = "Approve attack"

def attack_rollback(modeladmin, request, queryset):
    for game in queryset:
        if game.status is not Game.FINISHED:
            game.score = game.score - 1
            game_step = game.current_step
            if game_step.is_attack_approved:
                game_step.is_attack_approved = False
                game_step.save()
                game.mode = Game.ATTACK
                game.save()
approve_attack.short_description = "Approve attack"


def progress(obj):
    return f'{obj.score}/{obj.gamestep_set.count()}'
progress.short_description = "Progress"


def solving(obj):
    current_step = obj.current_step
    if current_step:
        if obj.mode == Game.CYPHER:
            return f'Puzzle - {current_step.step.puzzle.description}'
        elif obj.mode == Game.ATTACK:
            f'Attack - {current_step.step.attack.description}'
        else:
            return 'Mission'
    return '----'
solving.short_description = "Solving"


class GameStepInline(admin.TabularInline):
    model = GameStep

class GameAdmin(admin.ModelAdmin):
    inlines = [
        GameStepInline,
    ]
    list_display = ('user', progress, 'mode', 'status', solving, 'on_mission' )
    actions = [start_mission, end_mission, approve_attack]

    def changelist_view(self, request, extra_context=None):
        actions = self.get_actions(request)
        if (actions and request.method == 'POST' and 'index' in request.POST and
                request.POST['action'].endswith('mission')):
            data = request.POST.copy()
            data['select_across'] = '1'
            request.POST = data
            response = self.response_action(request, queryset=self.get_queryset(request))
            if response:
                return response
        return super(GameAdmin, self).changelist_view(request, extra_context)

class AttackAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'evidence_type', 'attack_uuid')


class PuzzleAdmin(admin.ModelAdmin):
    list_display = ('puzzle_type', 'description', 'tip', 'answer')

#TODO: start and end mission without select any player

admin.site.register(Attack, AttackAdmin)
admin.site.register(Puzzle, PuzzleAdmin)
admin.site.register(Station)
admin.site.register(Path, PathAdmin)
admin.site.register(Game, GameAdmin)
admin.site.register(Step)
admin.site.register(Story)
admin.site.register(Log)
