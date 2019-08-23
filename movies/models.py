from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=100,null=True)
    title_en = models.CharField(max_length=100,null=True)
    audience = models.IntegerField(null=True)
    open_date = models.DateField(null=True)
    genre = models.CharField(max_length=100,null=True)
    watch_grade = models.CharField(max_length=100,null=True)
    poster_url = models.TextField(null=True)
    score = models.FloatField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return f'{self.title} - {self.title_en}'

