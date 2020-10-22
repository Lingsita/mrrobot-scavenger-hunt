import uuid

from django.contrib.auth.models import User
from django.db import models


class Attack(models.Model):
    AUDIO = 'audio'
    VIDEO = 'video'
    EVIDENCE_TYPES = (
        (AUDIO, 'Audio'),
        (VIDEO, 'Video'),
    )
    attack_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    description = models.TextField()
    evidence_type = models.CharField(max_length=255, choices=EVIDENCE_TYPES)

    def __str__(self):
        return f"{self.description}"


class Puzzle(models.Model):
    description = models.TextField()
    answer = models.CharField(max_length=255)
    puzzle_type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.puzzle_type} - {self.description}"


class Station(models.Model):
    name = models.CharField(max_length=150, unique=True)
    place = models.TextField()

    def __str__(self):
        return f"{self.name}"

class Path(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Step(models.Model):
    class Meta:
        unique_together = ['order', 'path']

    order = models.IntegerField()
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    attack = models.ForeignKey(Attack, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.order}:{self.path}:{self.station}"


class GameStep(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    is_puzzle_solved = models.BooleanField(default=False)
    is_attack_approved = models.BooleanField(default=False)


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField('Score', null=True, blank=True)

    IN_PROGRESS = 'in_progress'
    FINISHED = 'finished'
    STATUS_CHOICES = (
        (IN_PROGRESS, 'In Progress'),
        (FINISHED, 'Finished'),
    )

    status = models.CharField(
        max_length=11,
        choices=STATUS_CHOICES,
        default=IN_PROGRESS
    )

    CYPHER = 'cypher'
    ATTACK = 'attack'
    MODE_TYPES = (
        (CYPHER, 'Cypher'),
        (ATTACK, 'Attack'),
    )
    mode = models.CharField(
        max_length=11,
        choices=MODE_TYPES,
        default=CYPHER
    )
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    path = models.ForeignKey(Path, on_delete=models.CASCADE)
    on_mission = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} - {self.status}'

    @property
    def get_current_station(self):
        return self.score + 1

    def start(self, user, path):
        for step in self.path.steps.all():
            GameStep.objects.create(game=self, step=step)
