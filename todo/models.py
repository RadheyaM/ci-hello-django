from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False, default="todo item")
    done = models.BooleanField(null=False, blank=False, default=False)

    def __str__(self):
        """represents itself with self.name"""
        return self.name

