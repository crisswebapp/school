# Generated by Django 3.0.8 on 2020-07-27 00:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20200726_1714'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='is_limit',
            new_name='is_limited',
        ),
    ]
