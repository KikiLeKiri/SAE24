import random
import time
import datetime
from paho.mqtt import client as mqtt_client

broker = 'broker.hivemq.com'
port = 1883
topic = "IUT/GR11/Colmar2023/SAE2.04/Maison1"
# Generate a Client ID with the publish prefix.
client_id = f'1025'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 1
    temp = 21.11
    while True:
        time.sleep(5)
        if (msg_count%10 == 0):
            temp_ajust = random.randint(-1,1)
            temp_ajust_mili = random.randint(-20,20)
            temp += (temp_ajust)+(temp_ajust_mili/100)
            temp = round(temp,2)
        jour = datetime.date.today().day
        mois = datetime.date.today().month
        annee = datetime.date.today().year
        temps = time.localtime()
        heure = time.strftime("%H:%M:%S", temps)
        msg = f"id_capteur={client_id},piece=sejour,date_={annee}-{mois}-{jour},heure={heure},temperature={temp}"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Send `{msg}` to topic `{topic}`")
        else:
            print(f"Failed to send message to topic {topic}")
        msg_count += 1

client = connect_mqtt()
client.loop_start()
publish(client)
client.loop_stop()
