# Generated by Django 2.1.4 on 2019-04-30 15:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='indications',
            unique_together={('date', 'area')},
        ),
    ]