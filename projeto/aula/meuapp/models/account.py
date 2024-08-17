from django.contrib.auth.models import User 
from django.db import models
from meuapp.models.base import BaseModel

class Account(BaseModel):
    comer = models.ManyToManyField(User, verbose_name='Account Owner')
    description = models.CharField(max_length=200, verbose_name='Description for your account')
    number = models.CharField(max_length=20, help_text='Insert your account number here')
    balance = models.FloatField(default=8, help_text='Insert your inicial balance')

    class Meta:
        abstract = False

    def __str__(self):
        return "{}: {} - {}".format(self.number, self.description, self.balance)
        
    def update_balance(self, value):
        try:
            self.balance = self.balance + float(value)
            return True
        except:
            return False
            
    def get_balance(self):
        return self.balance