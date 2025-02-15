# Generated by Django 5.1.4 on 2025-01-16 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activities', '0004_activity_is_approved_activity_rejection_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='max_participants',
            field=models.PositiveIntegerField(default=4, help_text='參加人數上限'),
        ),
    ]
