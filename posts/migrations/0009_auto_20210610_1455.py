# Generated by Django 3.0.4 on 2021-06-10 08:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0008_auto_20210610_1452'),
    ]

    operations = [
        migrations.RenameField(
            model_name='likecomment',
            old_name='created',
            new_name='created_at',
        ),
    ]
