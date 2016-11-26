import machine
import time

ledD2 = machine.Pin(4, machine.Pin.OUT)

for i in range(10):
    ledD2.high()
    time.sleep(0.5)
    ledD2.low()
    time.sleep(0.5)
