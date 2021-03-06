# Generated by Django 3.2 on 2021-04-25 02:47

from django.db import migrations, models
import roadmap.models


class Migration(migrations.Migration):

    dependencies = [
        ('roadmap', '0005_auto_20210425_0820'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='deadline',
            field=models.DateField(validators=[roadmap.models.validate_deadline_is_not_past]),
        ),
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateField(validators=[roadmap.models.validate_deadline_is_not_past]),
        ),
    ]
