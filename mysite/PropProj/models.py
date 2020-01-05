from django.db import models
class Drone(models.Model):
    Name = models.CharField(max_length=20, help_text="")
    Owner = models.CharField(max_length=20, help_text="")
    specs = models.ManyToManyField("Part", through='DronePart')

class Specs(models.Model):
    Name = models.CharField(max_length=20, help_text="")

    def __str__(self):
        return self.Name

class Part(models.Model):
    Name = models.CharField(max_length=20, help_text="")
    Type = models.CharField(max_length=20, help_text="")
    specs = models.ManyToManyField(Specs, through='PartSpecs')

    def __str__(self):
        return "{} ({})".format(self.Name, self.Type)

class DronePart(models.Model):
    DroneID = models.ForeignKey(Drone, on_delete=models.CASCADE)
    PartID = models.ForeignKey(Part, on_delete=models.CASCADE)



class PartSpecs(models.Model):
    SpecID = models.ForeignKey(Specs, on_delete=models.CASCADE)
    PartID = models.ForeignKey(Part, on_delete=models.CASCADE)
    value = models.CharField(max_length=30)

    def __str__(self):
        return "{} - {}: {}".format(self.SpecID.Name, self.PartID.Name, self.value)




