from django.db import models

class Department(models.Model):
    id = models.AutoField(primary_key=True)
    hotline_number = models.TextField()
    address = models.BinaryField()

class Responder(models.Model):
    first_name = models.IntegerField(primary_key=True)
    last_name = models.TextField()
    address = models.FloatField()
    gender = models.BinaryField()

class User(models.Model):
    phone_number = models.IntegerField(primary_key=True, unique=True)
    first_name = models.TextField()
    last_name = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='last_name')
    address = models.ForeignKey(Responder, on_delete=models.DO_NOTHING, db_column='address')
    age = models.BinaryField()

class Status(models.Model):
    cause_damage = models.IntegerField(primary_key=True, unique=True)
    cost_damage = models.TextField()
    description = models.TextField()
    start_date = models.TextField()
    end_date = models.TextField()
    start_time = models.TextField()
    end_time = models.TextField()

class Location(models.Model):
    address = models.IntegerField(primary_key=True, unique=True)
    zip_code = models.ForeignKey(Status, on_delete=models.DO_NOTHING, db_column='zip_code')
    location = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='location')
