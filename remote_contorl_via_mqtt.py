from umqtt.simple import MQTTClient
from machine import Pin
import ubinascii
import machine
import micropython


def do_connect():
    import network

    SSID = 'Your SSID'
    PASSWORD = 'Your password'

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('connecting to network...')
        sta_if.active(True)
        sta_if.connect(SSID, PASSWORD)
        while not sta_if.isconnected():
            pass
    print('Network configuration:', sta_if.ifconfig())

led = Pin(4, Pin.OUT, value=1)

# Default MQTT server to connect to
SERVER = "mqtt broker url or ip"
CLIENT_ID = ubinascii.hexlify(machine.unique_id())
TOPIC = b"Topic"
PORT_NO = 10449     #change to mqtt port no.
USERNAME = "id"
PASSWORD = "password"


state = 0

def sub_cb(topic, msg):
    global state
    print((topic, msg))
    if msg == b"on":
        led.value(1)
        state = 1
    elif msg == b"off":
        led.value(0)
        state = 0
    elif msg == b"toggle":
        # LED is inversed, so setting it to current state
        # value will make it toggle
        led.value(state)
        state = 1 - state


def main(server=SERVER):
    c = MQTTClient(CLIENT_ID, server, PORT_NO, USERNAME, PASSWORD, 60)
    # Subscribed messages will be delivered to this callback
    c.set_callback(sub_cb)
    c.connect()
    c.subscribe(TOPIC)
    print("Connected to %s, subscribed to %s topic" % (server, TOPIC))

    try:
        while 1:
            #micropython.mem_info()
            c.wait_msg()
    finally:
        c.disconnect()

if __name__ == '__main__':
#    load_config()
#    setup_pins()
    do_connect()
    main()
