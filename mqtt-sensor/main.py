import network
import time

from machine import unique_id
from ubinascii import hexlify
from sht30 import SHT30
from umqtt.simple import MQTTClient

def wifi_connect(ssid, pwd):
    """
    Connect to a wifi 'ssid' with password 'pwd'
    """

    sta_if = network.WLAN(network.STA_IF)
    ap_if = network.WLAN(network.AP_IF)
    if ap_if.active():
        ap_if.active(False)
    if not sta_if.isconnected():
        print('Connecting to network {}...'.format(ssid))
        sta_if.active(True)
        sta_if.connect(ssid, pwd)
        while not sta_if.isconnected():
            pass
        print("Connected!")
    return 'IP address: %s' % sta_if.ifconfig()[0]



if __name__ == "__main__":


    SSID = "<YOUR_SSID>"
    pwd = "<YOUR_PASSWORD>"
    mqtt_server = "<YOUR_MQTT_SERVER_HOSTNAME>"

    mqtt_client_id = "micropython-{}".format(hexlify(unique_id()).decode())
    print("mqtt_client_id:", mqtt_client_id)

    wifi_connect(SSID, pwd)
    client = MQTTClient(mqtt_client_id, mqtt_server)
    client.connect()
    sensor = SHT30()


    while True:
        time.sleep(1)
        temperature, humidity = sensor.measure()
        client.publish("{}/temperature".format(mqtt_client_id).encode(), "{:.2f}".format(float(str(temperature))).encode())
        client.publish("{}/humidity".format(mqtt_client_id).encode(), "{:.2f}".format(float(str(humidity))).encode())
