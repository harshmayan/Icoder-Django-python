# Generated by Django 3.2.19 on 2023-08-04 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_timestamp_blogcomment_timestamp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogcomment',
            old_name='perent',
            new_name='parent',
        ),
    ]