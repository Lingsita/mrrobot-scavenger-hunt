import uuid

from django.contrib.auth.models import User
from django.db import models


class Attack(models.Model):
    AUDIO = 'Audio'
    VIDEO = 'Video'
    FOTO = 'Foto'
    DOS_FOTOS = '2 Fotos'
    FOTO_VIDEO = '1 Foto y 1 Video'
    EVIDENCE_TYPES = (
        (AUDIO, AUDIO),
        (VIDEO, VIDEO),
        (DOS_FOTOS, DOS_FOTOS),
        (FOTO_VIDEO, FOTO_VIDEO),
        (FOTO, FOTO)
    )
    attack_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    title = models.TextField(null=True)
    description = models.TextField()
    evidence_type = models.CharField(max_length=255, choices=EVIDENCE_TYPES)

    def __str__(self):
        return f"{self.description}"


class Puzzle(models.Model):
    tip = models.TextField(null=True)
    description = models.TextField()
    answer = models.CharField(max_length=255)
    puzzle_type = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.puzzle_type} - {self.description}"


class Station(models.Model):
    name = models.CharField(max_length=150, unique=True)
    place = models.TextField()

    def __str__(self):
        return f"{self.name}:{self.place}"


class Path(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    url_image = models.CharField(max_length=255, null=True, blank=True)

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

    @property
    def next_step(self):
        try:
            return self.__class__.objects.get(path=self.path,
                                              order=self.order + 1)
        except self.__class__.DoesNotExist:
            return None


class Story(models.Model):
    name = models.CharField(max_length=150, unique=True)
    order = models.IntegerField()
    place = models.TextField()
    image = models.CharField(max_length=150, unique=True, help_text="image name")


class GameStep(models.Model):
    game = models.ForeignKey('Game', on_delete=models.CASCADE)
    step = models.ForeignKey(Step, on_delete=models.CASCADE)
    is_puzzle_solved = models.BooleanField(default=False)
    is_attack_approved = models.BooleanField(default=False)
    story = models.ForeignKey(Story, null=True, blank=True, on_delete=models.CASCADE)


class Game(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField('Score', default=0, blank=True)

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
    STORY = 'story'
    MODE_TYPES = (
        (CYPHER, 'Cypher'),
        (ATTACK, 'Attack'),
        (STORY, 'Story')
    )
    mode = models.CharField(
        max_length=11,
        choices=MODE_TYPES,
        default=STORY
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

    @property
    def current_step(self):
        try:
            return GameStep.objects.get(game=self,
                                             step__order=self.get_current_station)
        except:
            return None

    def start(self):
        for step in self.path.step_set.all():
            try:
                story = Story.objects.get(step_number=step.order)
            except:
                story = None
            GameStep.objects.create(game=self, step=step, story=story)

class Log(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'{self.created_on}: {self.message}'
