from django.db import models

# Create your models here.

class UserInfo(models.Model):
    username = models.CharField(max_length=20, null=False)
    userid = models.CharField(max_length=20, unique=True, null=False)
    userpw = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.username

class Board(models.Model):
    title = models.CharField(max_length=255, null=False)
    contents = models.TextField(max_length=1000, null=True)
    image = models.FileField()
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class Photo(models.Model):
    title = models.ForeignKey(Board,on_delete=models.CASCADE)
    image = models.FileField()

    def __str__(self):
        return self.title