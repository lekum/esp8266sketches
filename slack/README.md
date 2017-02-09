# ESP8266 Slack Button

## Installation

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
# Schematic

![schematic](https://github.com/lekum/esp8266sketches/blob/master/slack/circuit.png)
