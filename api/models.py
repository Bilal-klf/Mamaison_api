from django.db import models

class users(models.Model):
    name = models.CharField(max_length = 250)
    email = models.CharField(max_length = 250)
    password = models.CharField(max_length = 250)
    phone_number = models.CharField(max_length = 250)
    id = models.CharField(max_length = 100, primary_key = True)
    class Meta:
        db_table="users"


class house_data(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    windows = models.IntegerField()
    id = models.CharField(max_length = 100, primary_key = True)
    class Meta:
        db_table="house_data"