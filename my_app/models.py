from django.db import models

# Create your models here.

class Customer(models.Model):
    customerid = models.IntegerField(db_column='CustomerId', primary_key=True)  # Field name made lowercase.
    customername = models.CharField(db_column='CustomerName', max_length=50)  # Field name made lowercase.
    address = models.ForeignKey("City", on_delete =models.SET_DEFAULT,default = 'null' ,db_column='Address', max_length=50, blank=True, null=True)  # Field name made lowercase.
    blance = models.IntegerField(db_column='Blance', blank=True, null=True)  # Field name made lowercase.
    phone = models.CharField(max_length=13, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'

class City(models.Model):
    city_id = models.IntegerField(db_column='City id', primary_key=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    cityname = models.CharField(db_column='CityName', unique=True, max_length=45, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.cityname

