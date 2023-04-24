from django.shortcuts import render
from django.http import HttpResponse
from django.utils import timezone


# Create your views here.ort


def index(request):
    tz = timezone.get_current_timezone()
    tnow = timezone.datetime.now(tz=tz)
    cdate = tnow.date()
    ctime = cdate.ctime()

    return HttpResponse(f" {cdate} \n  {ctime} \n Hello!!, With Metrorail we will take you there Nomakanjani!!")
