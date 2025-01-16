# Generated by Django 5.1.4 on 2025-01-16 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='membership_level',
            field=models.CharField(choices=[('Basic', '基本會員'), ('Silver', '銀級會員'), ('Gold', '金級會員'), ('Platinum', '白金會員')], default='Basic', max_length=10),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', '男性'), ('female', '女性'), ('other', '多元性別')], max_length=10, null=True),
        ),
    ]
