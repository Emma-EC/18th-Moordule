# Generated by Django 5.1.4 on 2025-01-07 07:22

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('activities', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='owner',
            field=models.ForeignKey(help_text='聚會建立者', on_delete=django.db.models.deletion.CASCADE, related_name='created_activities', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='category',
            field=models.ForeignKey(blank=True, help_text='聚會分類', null=True, on_delete=django.db.models.deletion.SET_NULL, to='activities.category'),
        ),
        migrations.AddField(
            model_name='meetuppaticipat',
            name='activity',
            field=models.ForeignKey(help_text='聚會', on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='activities.activity'),
        ),
        migrations.AddField(
            model_name='meetuppaticipat',
            name='participant',
            field=models.ForeignKey(help_text='參與者', on_delete=django.db.models.deletion.CASCADE, related_name='meetups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='meetuppaticipat',
            unique_together={('activity', 'participant')},
        ),
    ]
