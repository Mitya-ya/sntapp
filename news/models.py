from django.db import models
from django.utils import timezone
import bbcode


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now)

    class Meta:
        ordering = ["-created_date"]

    def __str__(self):
        return self.title

    @property
    def txt(self):
        return bbcode.render_html(self.text)

    @property
    def Title(self):
        return self.title.capitalize()


class Area(models.Model):
    number = models.CharField(primary_key=True, max_length=20)
    owner = models.CharField(max_length=250)
    dir_fl = models.BooleanField(default=False)
    job = models.TextField(max_length=250, default="")

    def __str__(self):
        return self.owner + ' (' + self.number + ')'


class IndicationsDate(models.Model):
    date = models.DateField(primary_key=True)
    note = models.TextField(max_length=250)

    def __str__(self):
        return self.date.strftime('%Y-%m-%d')


class Indications(models.Model):
    date = models.ForeignKey('IndicationsDate', on_delete=models.CASCADE)
    area = models.ForeignKey('Area', on_delete=models.CASCADE)
    T1 = models.FloatField(default=0)
    T2 = models.FloatField(default=0)

    def __str__(self):
        return self.area.number + ' ' + self.date.date.strftime('%Y-%m-%d') + ' ' + str(self.T1) + '/' + str(self.T2)

    class Meta:
        unique_together = (("date", "area"),)
    #    index_together = [["date", "area"], ]


class Subscriber(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email


