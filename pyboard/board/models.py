from django.db import models
from datetime import datetime

# Create your models here.


class Board(models.Model):
    bno = models.AutoField(primary_key=True)
    writer = models.CharField(null=False, max_length=50)
    title = models.CharField(null=False, max_length=120)
    content = models.TextField(null=False)
    hit = models.IntegerField(default = 0)
    post_date = models.DateTimeField(default = datetime.now, blank=True)
    filename = models.CharField(null=True, blank=True, default='', max_length=500)
    filesize=models.IntegerField(default=0)
    down=models.IntegerField(default=0)
    
    def hit_up(self):
        self.hit += 1
    def down_up(self):
        self.down += 1  
class Comment(models.Model):
    #댓글 글번호
    cno = models.AutoField(primary_key=True)
    #게시물 번호
    bno = models.IntegerField(null=False)
    writer=models.CharField(null=False,max_length=50)
    content=models.TextField(null=False)
    post_date=models.DateTimeField(default=datetime.now,blank=True)