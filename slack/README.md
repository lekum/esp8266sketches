# ESP8266 Slack Button

## Arduino version

Populate the variables in the sketch:

```
/*
 CIRCUIT CONFIGURATION
 */
const int ledPin = D3;
const int buttonPin = D6;

/*
 WIFI CONFIGURATION
 */
const String SSID = "<YOUR_SSID>"
const String pwd = "<YOUR_PASSWORD>"

/*
 SLACK CONFIGURATION
 */
const String slack_hook_url = "<SLACK_HOOK_URL>";
const String slack_icon_url = "<SLACK_ICON_URL>";
const String slack_message = "<SLACK_MESSAGE>";
const String slack_username = "<SLACK_USERNAME>";
```

Upload the sketch `slack.ino`

## MicroPython version

### Installation of the MicroPython firmware

Download a [firmware for the ESP8266](http://micropython.org/download#esp8266).

Install `esptool.py`:

```
python3 -m venv esptool
source esptool/bin/activate
(esptool) pip install esptool
```

Connect the board and take note of the port (e.g. `/dev/ttyUSB0`) that shows up in the ouput of `dmesg` command.

Erase the flash memory of the board:

```
esptool.py --port /dev/ttyUSB0 erase_flash
```

Flash with the firmware:

```
esptool.py --port /dev/ttyUSB0 write_flash -fm dio -fs 32m 0 esp8266-20170108-v1.8.7.bin
```

Install `picocom` and connect to the serial interface:

```
picocom -b 115200 /dev/ttyUSB0
```

You should see the MicroPython REPL:

```
MicroPython v1.8.7-7-gb5a1a20a3 on 2017-01-09; ESP module with ESP8266
Type "help()" for more information.
>>>
```

In case you don't see it, do a button restart of the board and try again.

### Deployment of the script

Populate the variables in the script `main.py`:

```
SSID = "<YOUR_SSID>"
pwd = "<YOUR_PASSWORD>"
slack_hook_url = "<SLACK_HOOK_URL>"
slack_icon_url = "<SLACK_ICON_URL>"
slack_message = "<SLACK_MESSAGE>"
slack_username = "<SLACK_USERNAME>"
```

Upload the script using, for example, `webrepl`. In order to enable it, connect to the MicroPython REPL via `picocom` and run:
```
import webrepl_setup
Would you like to (E)nable or (D)isable it running on boot?
(Empty line to quit)
>
```

Press `(E)nable` and set a password.

Now, connect the ESP to a WiFi. Run:

```
sta_if = network.WLAN(network.STA_IF)
sta_if.active(True)
sta_if.connect("<YOUR_SSID>", "<YOUR_PASSWORD>")
print('IP address:', sta_if.ifconfig()[0])
```
Take note of the IP address.

Download the [webrpl client](https://github.com/micropython/webrepl) and run this to upload the `main.py` file:

```
./webrepl_cli.py main.py <YOUR_IP>:/main.py
```

# Schematic

![schematic](https://github.com/lekum/esp8266sketches/blob/master/slack/circuit.png)
