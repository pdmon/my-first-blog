# Generated by Django 3.0.dev20190330204916 on 2019-04-04 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20190404_0714'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='comment_author',
            field=models.CharField(max_length=15, null=True),
        ),
    ]
