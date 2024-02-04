# SPDX-FileCopyrightText: 2024 Mike Causer <https://github.com/mcauser>
# SPDX-License-Identifier: MIT

"""
MicroPython HDC1080 Basic example

Prints the temperature and humidity every 500ms
"""

from machine import I2C
from hdc1080 import HDC1080

i2c = I2C(0)
hdc = HDC1080(i2c)

from time import sleep_ms

hdc.config(humid_res=14, temp_res=14, mode=0, heater=0)

if hdc.check():
    print(f"Found HDC1080 with serial number {hdc.serial_number()}")

while True:
    print(f"{hdc.temperature()} C, {hdc.humidity()} RH")
    sleep_ms(500)
