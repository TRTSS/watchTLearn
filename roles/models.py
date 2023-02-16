from django.db import models

# Create your models here.
class Role(models.Model):
    rolePower = models.IntegerField(default=0)
    roleTitle = models.CharField(max_length=255, default='Новая роль')

    def __str__(self):
        return self.roleTitle

    def GetPower(self):
        return self.rolePower