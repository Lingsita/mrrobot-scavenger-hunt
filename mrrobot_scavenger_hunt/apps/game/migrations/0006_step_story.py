# Generated by Django 3.1.2 on 2020-10-24 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0005_remove_step_next'),
    ]

    operations = [
        migrations.AddField(
            model_name='step',
            name='story',
            field=models.TextField(blank=True, null=True),
        ),
    ]
