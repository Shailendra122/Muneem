from django.db import models
from django.forms import DateField

class Account_Data(models.Model):
    u_name=models.CharField(max_length=100)
    d_or_c=models.CharField(max_length=10)
    name=models.CharField(max_length=100)
    m_no=models.CharField(max_length=10)
    date=models.DateField()
    amount=models.FloatField()
    paid=models.CharField(max_length=10,default='Not paid',null=True)
    date_of_transaction=models.DateField(blank=True,null=True)