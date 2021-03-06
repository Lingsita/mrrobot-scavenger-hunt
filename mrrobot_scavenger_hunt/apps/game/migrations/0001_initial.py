# Generated by Django 3.1.2 on 2020-10-22 03:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attack',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attack_uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('description', models.TextField()),
                ('evidence_type', models.CharField(choices=[('audio', 'Audio'), ('video', 'Video')], max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(blank=True, null=True, verbose_name='Score')),
                ('status', models.CharField(choices=[('in_progress', 'In Progress'), ('finished', 'Finished')], default='in_progress', max_length=11)),
                ('mode', models.CharField(choices=[('cypher', 'Cypher'), ('attack', 'Attack')], default='cypher', max_length=11)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateTimeField(blank=True, null=True)),
                ('on_mission', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Path',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Puzzle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('answer', models.CharField(max_length=255)),
                ('puzzle_type', models.CharField(blank=True, max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
                ('place', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField()),
                ('attack', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.attack')),
                ('path', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.path')),
                ('puzzle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.puzzle')),
                ('station', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.station')),
            ],
        ),
        migrations.CreateModel(
            name='GameStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_puzzle_solved', models.BooleanField(default=False)),
                ('is_attack_approved', models.BooleanField(default=False)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.game')),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.step')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='path',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.path'),
        ),
        migrations.AddField(
            model_name='game',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
