# Generated by Django 2.1.4 on 2019-03-27 21:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_auto_20190328_0051'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='indications',
            unique_together={('date', 'area')},
        ),
        migrations.AlterIndexTogether(
            name='indications',
            index_together=set(),
        ),
    ]