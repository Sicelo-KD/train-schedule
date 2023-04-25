
import os
import sys
from abc import ABC

import pandas as pd
from django.core.management.base import BaseCommand, CommandError
from metrorail.models import Province


# province = Province(name="GAUTENG")
# region = Region(region="Pretoria", province_id=province)
# route = Route(route_code="M01", region=region)
# Station = Station(station_name="Mabopane")


class Command(BaseCommand):
    dir = ""

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)
        #management/commands/csv_datasource/provinces/gauteng/regions/pretoria/Sunday-Mabopane-Pretoria.csv

    def handle(self, *args, **options):
        path = options["path"]
        base_path = "/home/sicelo/myWork/personal_projects/train_schedule/"
        absolute_path = base_path + "metrorail/files/csv_datasource/provinces/gauteng/regions/pretoria/Sunday-Mabopane-Pretoria.csv"
        file = pd.read_csv(absolute_path)

        try:
            province = Province.objects.get(pk=1)
        except Province.DoesNotExist:
            raise CommandError("NOT FOUND")

        self.stdout.write(
            province.name
        )
        #self.stdout.write(
        #    self.style.SUCCESS(file.values)
        #)
