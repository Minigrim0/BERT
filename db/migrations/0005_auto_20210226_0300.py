# Generated by Django 3.1.6 on 2021-02-26 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0004_reminder_guild'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reminder',
            name='name',
            field=models.CharField(default='none', max_length=150, unique=True),
        ),
    ]