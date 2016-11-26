import machine
import time

pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
adc = machine.ADC(0)
while True:
    i=adc.read()
    print(i)
    pwm.duty(i)
    time.sleep(0.1)
