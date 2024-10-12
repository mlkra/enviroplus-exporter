#!/usr/bin/env python3

import argparse
import time
from collections.abc import Generator

from bme280 import BME280
from enviroplus import gas
from ltr559 import LTR559
from prometheus_client import Gauge, start_http_server
from smbus2 import SMBus

# Prometheus gauges
comp_temp_gauge = Gauge("comp_temp", "Compensated temperature")
pressure_gauge = Gauge("pressure", "Pressure")
humidity_gauge = Gauge("humidity", "Humidity")
illuminance_gauge = Gauge("illuminance", "Illuminance")
prox_gauge = Gauge("prox", "Proximity")
ox_gauge = Gauge("ox", "Oxidising gas")
red_gauge = Gauge("red", "Reducing gas")
nh3_gauge = Gauge("nh3", "NH3 gas")

# Based on https://github.com/pimoroni/enviroplus-python/blob/main/examples
bme280 = BME280(i2c_dev=SMBus(1))
ltr559 = LTR559()


def get_cpu_temp() -> float:
    with open("/sys/class/thermal/thermal_zone0/temp", "r") as f:
        return int(f.read()) / 1000.0


def get_comp_temp(factor=1.3, cpu_temps=[get_cpu_temp()] * 5) -> float:
    cpu_temp = get_cpu_temp()
    cpu_temps = cpu_temps[1:] + [cpu_temp]
    raw_temp = bme280.get_temperature()
    return raw_temp - (((sum(cpu_temps) / float(len(cpu_temps))) - raw_temp) / factor)


###############################################################################


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--sleep-time", type=int, default=1)
    args = parser.parse_args()
    sleep_time = args.sleep_time

    start_http_server(8000)
    while True:
        comp_temp_gauge.set(get_comp_temp())
        pressure_gauge.set(bme280.get_pressure())
        humidity_gauge.set(bme280.get_humidity())
        illuminance_gauge.set(ltr559.get_lux())
        prox_gauge.set(ltr559.get_proximity())
        gas_readings = gas.read_all()
        ox_gauge.set(gas_readings.oxidising)
        red_gauge.set(gas_readings.reducing)
        nh3_gauge.set(gas_readings.nh3)
        time.sleep(sleep_time)


if __name__ == "__main__":
    main()
