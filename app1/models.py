from django.db import models

# Create your models here.
class Django(models.Model):
    trainer=models.CharField(max_length=100)
    no_of_students=models.IntegerField()

    def __str__(self):
        return self.trainer
    
    