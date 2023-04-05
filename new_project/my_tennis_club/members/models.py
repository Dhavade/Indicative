from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
percentage_validators=[MinValueValidator(0.9), MaxValueValidator(100)]

# Create your models here.
class Member(models.Model):
    firstname=models.CharField(max_length=225)
    lastname=models.CharField(max_length=225)

'''class file(models.Model):
    file=models.FileField(uplode_to='files')    '''

'''class Productfield(models.Model):
    Coupon_Rate=models.FloatField()
    ISIN=models.TextField()
    Name_of_the_security=models.CharField(max_length=225)
    CATEGORY=models.CharField(max_length=225)
    Rating_Agency=models.CharField(max_length=225)
    Maturity_Date=models.CharField(max_length=225)
    IP_Dates=models.CharField(max_length=225)
    Put_Call_Option=models.TextField()
    Price_Per_100=models.FloatField()
    YTM=models.FloatField()
    YTC_YTP=models.TextField()
    Face_Value=models.CharField(max_length=225)
    Quantum=models.CharField(max_length=225)
    ip_dates=models.TextField()
    class Meta:
        db_table = "Product Brande"'''
    
from django.db import models

class Person1(models.Model):
    ip = models.TextField()
    date = models.TextField()

    
    #objects = models.Manager()
    '''def __str__(self):
        return f"File id: {self.id}"'''
'''class update_data(models.model):
    Coupon_Rate=models.FloatField()
    ISIN=models.TextField()
    Name_of_the_security=models.CharField(max_length=225)
    CATEGORY=models.CharField(max_length=225)
    Rating_Agency=models.CharField(max_length=225)
    Maturity_Date=models.CharField(max_length=225)
    IP_Dates=models.CharField(max_length=225)
    Put_Call_Option=models.TextField()
    Price_Per_100=models.FloatField()
    YTM=models.FloatField()
    YTC_YTP=models.TextField()
    Face_Value=models.CharField(max_length=225)
    Quantum=models.CharField(max_length=225)'''
    