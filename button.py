import machine
import time

ledD2 = machine.Pin(4, machine.Pin.OUT)
button = machine.Pin(12, machine.Pin.IN, machine.Pin.PULL_UP)
while True:
    first = button.value()
    time.sleep(0.01)
    second = button.value()
    if first and not second:
        print('Button pressed!')
        ledD2.high()
    elif not first and second:
        print('Button released!')
        ledD2.low()

