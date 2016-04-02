from django.db import models
from django.utils import timezone


class Skill(models.Model):
    name = models.CharField(max_length=200, primary_key=True)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Profile(models.Model):
    url = models.CharField(max_length=200, default='', primary_key=True)
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    current_position = models.TextField()
    summary = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    count_top_skills = models.IntegerField(default=0)
    skills = models.ManyToManyField(Skill)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.url + "::" + self.name +"::" +self.title



