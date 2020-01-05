from django.db import models
class Drone(models.Model):
    Name = models.CharField(max_length=20, help_text="")
    Owner = models.CharField(max_length=20, help_text="")
class Part(models.Model):
    Name = models.CharField(max_length=20, help_text="")
    Type = models.CharField(max_length=20, help_text="")
class Specs(models.Model):
    Name = models.CharField(max_length=20, help_text="")
class DronePart(models.Model):
    DroneID = models.IntegerField(max_length=20, help_text="")
    PartID = models.IntegerField(max_length=20, help_text="")
class PartSpecs(models.Model):
    SpecID = models.IntegerField(max_length=20, help_text="")
    PartID = models.IntegerField(max_length=20, help_text="")