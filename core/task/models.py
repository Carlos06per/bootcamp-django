from django.db import models

class Priority(models.Model):
    name = models.CharField(max_length = 40)
    def __str__(self):
        return self.name

# Create your models here.
class task(models.Model):
    title = models.CharField(max_length=60, null = False)
    description= models.CharField(max_length = 150, null = True)
    is_completed = models.BooleanField(default = False)
    priority = models.ForeignKey(Priority, on_delete = models.DO_NOTHING)

    def __str__(self):
        return self.title