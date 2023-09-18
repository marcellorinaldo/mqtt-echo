# mqtt-echo

This project is a collection of simple MQTT clients written in different languages that connect to a broker and display in terminal the messages arriving at a certain topic.

Implemented languages:
- [Python](./python/README.md)

## Mosquitto broker setup (macOS)

The MQTT broker [mosquitto](https://mosquitto.org/) can be installed on MacOS with:

```bash
brew install mosquitto
```

The broker can be run with:

```bash
/usr/local/opt/mosquitto/sbin/mosquitto -c ./mosquitto.conf
```

where `./mosquitto.conf` is a simple configuration file contained in this repo.

The broker will listen on default port 1883 and accept all connections. No username and passwords are required. To stop the broker simply press CMD-C.