from django.db import models
# Create your models here.

class Tiers(models.Model):
    tier = models.IntegerField()
    bpuLimiter = models.IntegerField()
    special = models.IntegerField() #noting this here: this can be a single digit multiplied later on to add HP

class Frames(models.Model):
    frame = models.CharField(max_length=30)
    size = models.CharField(max_length=12)
    maneuverability = models.CharField(max_length=30)
    hp = models.IntegerField()
    increment = models.IntegerField()
    dt = models.IntegerField()
    ct = models.IntegerField()
    mounts = models.CharField(max_length=150)
    expansionBays = models.IntegerField()
    minimumCrew = models.IntegerField()
    maximumCrew = models.IntegerField()
    cost = models.IntegerField()

class PowerCores(models.Model):
    core = models.CharField(max_length=30)
    size = models.CharField(max_length=12)
    pcu = models.IntegerField()
    cost = models.IntegerField()

class Thrusters(models.Model):
    thruster = models.CharField(max_length=30)
    size = models.CharField(max_length=1)
    speed = models.IntegerField()
    piloting = models.IntegerField()
    pcu = models.IntegerField()
    cost = models.IntegerField()

class Armors(models.Model):
    armor = models.CharField(max_length=30)
    ac = models.IntegerField()
    specialTL = models.IntegerField()
    specialTD = models.IntegerField()
    cost = models.IntegerField()

class Computers(models.Model):
    computer = models.CharField(max_length=30)
    bonus = models.CharField(max_length=12)
    nodes = models.IntegerField()
    pcu = models.IntegerField()
    cost = models.IntegerField()

class CrewQuarters(models.Model):
    crewQuarters = models.CharField(max_length=10)
    cost = models.IntegerField()

class DefensiveCountermeasures(models.Model):
    defensiveCountermeasures = models.CharField(max_length=15)
    TLbonus = models.IntegerField()
    pcu = models.IntegerField()
    cost = models.IntegerField()

class DriftEngines(models.Model):
    driftEngine = models.CharField(max_length=20)
    rating = models.IntegerField()
    pcuRequirement = models.IntegerField()
    maxSize = models.CharField(max_length=12)
    cost = models.IntegerField()

class ExpansionBays(models.Model):
    expansionBay = models.CharField(max_length=50)
    pcu = models.IntegerField()
    cost = models.IntegerField()

class Security(models.Model):
    security = models.CharField(max_length=60)
    cost = models.CharField(max_length=36)

class Sensors(models.Model):
    sensors = models.CharField(max_length=36)
    range = models.CharField(max_length=12)
    modifier = models.IntegerField()
    cost = models.IntegerField()

class Shields(models.Model):
    shield = models.CharField(max_length=24)
    totalSP = models.IntegerField()
    regen = models.CharField(max_length=12)
    pcu = models.IntegerField()
    cost = models.IntegerField()

class Weapons(models.Model):
    weapon = models.CharField(max_length=48)
    weaponClass = models.CharField(max_length=12) #light, heavy, capital
    weaponType = models.CharField(max_length=12) #direct, tracking
    speed = models.IntegerField() #only applies to tracking weapons
    range = models.CharField(max_length=12)
    damage = models.CharField(max_length=12)
    pcu = models.IntegerField()
    cost = models.IntegerField()
    special = models.CharField(max_length=36)

class PersonnelWeaponsLongarm(models.Model):
    weapon = models.CharField(max_length=48)
    level = models.IntegerField()

class PersonnelWeaponsHeavy(models.Model):
    weapon = models.CharField(max_length=48)
    level = models.IntegerField()

# class CustomSelect(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     powercore = models.ForeignKey(PowerCores, on_delete=models.CASCADE, null =True)
#     thruster = models.ForeignKey(Thrusters, on_delete=models.CASCADE, null =True)
#     armor =models.ForeignKey(Armors, on_delete=models.CASCADE, null =True)
#     computer =models.ForeignKey(Computers, on_delete=models.CASCADE, null =True)
#     crewQuarter = models.ForeignKey(CrewQuarters, on_delete=models.CASCADE, null =True)
#     defensiveCountermasure = models.ForeignKey(DefensiveCountermeasures, on_delete=models.CASCADE, null =True)
#     driftEngine = models.ForeignKey(DriftEngines, on_delete=models.CASCADE, null =True)
#     expansionBay = models.ForeignKey(ExpansionBays, on_delete=models.CASCADE, null =True)
#     security = models.ForeignKey(Security, on_delete=models.CASCADE, null =True)
#     sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE, null =True)
#     shield = models.ForeignKey(Shields, on_delete=models.CASCADE, null =True)
#     weapon = models.ForeignKey(Weapons, on_delete=models.CASCADE, null =True)
