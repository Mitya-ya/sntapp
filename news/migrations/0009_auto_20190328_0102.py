# Generated by Django 2.1.4 on 2019-03-27 22:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0008_auto_20190328_0057'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='indications',
            unique_together={('date', 'area')},
        ),
    ]
