from django.shortcuts import render
import psutil
import time
import threading
from datetime import datetime
from json import dumps
from django.core import serializers
from CPULoad.models import AverageLoad, InstantLoad


def calculate():

    avg_load_list = []
    interval = 5
    counter = 0
    while True:

        dt = datetime.now()

        instant_load_model = InstantLoad()
        # запись загрузки процессора с помощью psutil
        instant_load = psutil.cpu_percent(interval)
        instant_load_model.cpu_load = instant_load
        instant_load_model.time = datetime.timestamp(dt)
        instant_load_model.save()

        average_load = AverageLoad()
        avg_load_list.append(instant_load)
        counter += 1

        if counter > 12:
            average_load.cpu_load = sum(avg_load_list) / len(avg_load_list)
            average_load.time = datetime.timestamp(dt)
            average_load.save()
            counter = 0
            avg_load_list = []

def CPULoad(request):

    # отдельный поток
    t = threading.Thread(target=calculate, args=())
    t.start()

    instant_count = 720
    average_count = 60

    # моментальная загрузка
    instant_load = InstantLoad.objects.all()[len(InstantLoad.objects.all())-instant_count:]
    # усредненная загрузка (1 мин)
    average_load = AverageLoad.objects.all()[len(AverageLoad.objects.all())-average_count:]

    instant_load_json = serializers.serialize("json", instant_load)
    average_load_json = serializers.serialize("json", average_load)

    return render(request, 'index.html', {"instant_load": instant_load_json, "average_load": average_load_json})

