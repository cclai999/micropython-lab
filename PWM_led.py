import time
import machine
pwm = machine.PWM(machine.Pin(15))
pwm.freq(60)
while True:
    for i in range(1024):
        pwm.duty(i)
        time.sleep(0.005)
    for i in range(1023, -1, -1):
        pwm.duty(i)
        time.sleep(0.005)
