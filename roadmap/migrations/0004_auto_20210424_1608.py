# Generated by Django 3.2 on 2021-04-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0003_auto_20210424_1209'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goal',
            options={'ordering': ['-created_at']},
        ),
        migrations.AddField(
            model_name='task',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
