# Generated by Django 3.1.2 on 2020-11-07 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20201102_1349'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attack',
            name='evidence_type',
            field=models.CharField(choices=[('Audio', 'Audio'), ('Video', 'Video'), ('2 Fotos', '2 Fotos'), ('1 Foto y 1 Video', '1 Foto y 1 Video'), ('Foto', 'Foto')], max_length=255),
        ),
    ]
