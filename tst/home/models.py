from django.db import models
import random , string

# Create your models here.
def randz(seed):
    rz = '' 
    for i in range(seed):
        rz = rz + random.choice(string.ascii_letters)
    return rz


class myBlogContent(models.Model):
    blogTitle = models.CharField(max_length=50)
    blogContent = models.CharField(max_length=1000)
    blogDate = models.DateTimeField(auto_now_add=True)
    blogID= models.CharField(default=randz(6))

    def __str__(self):
        return f"{self.blogTitle} at {self.blogDate} ID: {self.blogID}"