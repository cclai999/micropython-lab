import machine
import time


adc = machine.ADC(0)
while True:
    print(adc.read())
    time.sleep(0.5)
