# Generated by Django 3.2.19 on 2023-08-04 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_perent_blogcomment_parent'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='timeStamp',
            new_name='timestamp',
        ),
    ]
