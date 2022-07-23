from django.db import models

# Create your models here.


class Category(models.Model):
    name=models.CharField(max_length=255, blank=False)

class Post(models.Model):
    title=models.CharField(max_length=255, blank=False)
    content=models.TextField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE, default=1)

    def __str__(self):
        return(f'{self.title} {self.content}')
