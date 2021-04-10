from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Profile(models.Model):
    name=models.ForeignKey(User,on_delete=models.CASCADE)
    monthly_limit=models.FloatField(default=0)
    expenses_soFar=models.FloatField(default=0)

    def __str__(self):
        return str(self.name)
    


class Records(models.Model):
    expenditure_user=models.ForeignKey(User,on_delete=models.CASCADE)
    expenditure_name=models.CharField(max_length=100)
    expenditure_type=models.CharField(max_length=100)
    expenditure_date=models.DateField()
    expenditure_amount=models.FloatField

    def __str__(self):
    	return str(self.expenditure_user)
    
