import paho.mqtt.client as mqtt
import argparse
from termcolor import colored

parser = argparse.ArgumentParser(
    prog="MQTT Client Echo 0.1.0.",
    description="Subscribes on a topic and prints all messages arriving on it.",
    epilog="Example usage: python3 client.py --host 'localhost' --topic '$EDC/test/E4:5F:01:35:7F:F4/#'."
)

parser.add_argument(
    "--host",
    help="Host to connect to on port 1883, defaults to 'localhost'.",
    default="localhost",
    required=False
)

parser.add_argument(
    "--topic",
    help="Topic to subscribe on.",
    required=True
)

args = parser.parse_args()

def print_connection_successful(host, return_code, topic):
    print("Connected to", end=" ")
    print(colored(host + ":1883", color="green"), end=" ")
    print("with result code", end=" ")
    print(colored(return_code, color="green"), end=" ")
    print("on topic: ", end="'")
    print(colored(topic, color="green"), end="")
    print("'.\n")

def print_message(topic, payload):
    print("Message arrived on topic", end=": '")
    print(colored(topic, color="light_green"), end="'.\n")
    print(colored(payload, color = "light_blue"), end="\n\n")

def on_connect(client, userdata, flags, rc):
    client.subscribe(args.topic)
    print_connection_successful(args.host, str(rc), args.topic)

def on_message(client, userdata, msg):
    print_message(msg.topic, str(msg.payload))

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(args.host, 1883, 60)
client.loop_forever()