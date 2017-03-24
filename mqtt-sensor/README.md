# ESP8266 temperature and humidity sensor

## Schematic

Just connect the [SHT30](https://www.wemos.cc/product/sht30-shield.html) shield to the [Wemos D1 Mini Pro](https://www.wemos.cc/product/d1-mini-pro.html).

## Settings

Populate the variables in the script `main.py`:

```
SSID = "<YOUR_SSID>"
pwd = "<YOUR_PASSWORD>"
mqtt_server = "<YOUR_MQTT_SERVER_HOSTNAME>"

```

## Deployment

Upload `main.py` and `sht30.py` to your board. Attach a serial cable if you want to read debug information, as the `mqtt_client_id`. The topics in which temperature and humidity are published are:

- `<mqtt_client_id>/temperature`
- `<mqtt_client_id>/humidity`

## Attribution

The file `sht30.py` belongs to [this](https://github.com/rsc1975/micropython-sht30) repo (by Roberto Sánchez, under Apache License 2.0).
