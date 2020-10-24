# Generated by Django 3.1.2 on 2020-10-24 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_auto_20201022_0442'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='next',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='game',
            name='score',
            field=models.IntegerField(blank=True, default=0, verbose_name='Score'),
        ),
    ]