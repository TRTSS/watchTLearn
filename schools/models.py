from django.db import models


# Create your models here.
class School(models.Model):
    schoolName = models.CharField(max_length=255, verbose_name="Название школы", default="Новая школа")

    def __str__(self):
        return self.schoolName