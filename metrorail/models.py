from django.db import models


# Create your models here.
class Province(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self): return f"{self.name}"


class Region(models.Model):
    region = models.CharField(max_length=64, unique=True)
    province_id = models.ForeignKey(Province, on_delete=models.deletion.CASCADE)

    def __str__(self): return f"{self.region}\t{self.province_id}"


class Route(models.Model):
    route_code = models.CharField(max_length=3)
    region = models.ForeignKey(Region, on_delete=models.deletion.CASCADE)

    def __str__(self): return f"{self.route_code} \n {self.region}"


class Station(models.Model):
    station_name = models.CharField(max_length=64)

    def __str__(self): return f"{self.station_name}"


class Train(models.Model):
    DAY_OF_WEEK = [("WK", "WEEKDAY"),
                   ("SUN", "SUNDAY"),
                   ("SAT", "SATURDAY")
                   ]
    DIRECTION = [("UP", "UP"), ("DOWN", "DOWN")]
    train_number = models.CharField(max_length=4)
    direction = models.CharField(max_length=4, choices=DIRECTION)
    day_of_week = models.CharField(max_length=3, choices=DAY_OF_WEEK)
    route = models.ForeignKey(Route, on_delete=models.deletion.CASCADE)
    stations = models.ManyToManyField(Station, through="ArrivalTime")

    def __str__(self):
        return f"{self.train_number} \n " \
               f"{self.direction} \n " \
               f"{self.route} \n" \
               f"{self.day_of_week} \n" \
               f"{self.stations}"


class ArrivalTime(models.Model):
    arrival_time = models.TimeField()
    train = models.ForeignKey(Train, on_delete=models.deletion.CASCADE)
    station = models.ForeignKey(Station, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return f"{self.train} \t {self.station} \t {self.arrival_time}"
