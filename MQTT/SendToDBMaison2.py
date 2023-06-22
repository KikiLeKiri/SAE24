from paho.mqtt import client as mqtt_client
import MySQLdb
import time

db_connection = None
cursor = None
message_cache = []  # Cache for storing messages during database disconnection

# MQTT Settings
MQTT_Broker = 'broker.hivemq.com'
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "IUT/GR11/Colmar2023/SAE2.04/Maison2"

# Database connection function
def connect_to_database():
    global db_connection, cursor
    try:
        db_connection = MySQLdb.connect(host='localhost', user='root', passwd='toto', db='mqttdb')
        cursor = db_connection.cursor()
        print("Connected to the database")
        process_message_cache()  # Process cached messages if any
    except MySQLdb.Error as error:
        print("Error connecting to the database: {}".format(error))
        retry_connection()  # Retry connection after a delay

# Retry connection to the database after a delay
def retry_connection():
    global db_connection, cursor
    print("Retrying database connection in 5 seconds...")
    time.sleep(5)
    connect_to_database()

# Subscribe
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        client.subscribe(MQTT_Topic, 0)
        print("Subscribed to MQTT Topic: {}".format(MQTT_Topic))
    else:
        print("Failed to connect to MQTT Broker")

def on_message(client, userdata, msg):
    print("Received message =", str(msg.payload.decode("utf-8")))
    message_recu = str(msg.payload.decode("utf-8"))
    message = message_recu.split(',')
    colone = []
    valeur = []
    for e in message:
        temp = e.split('=')
        colone.append(temp[0])
        valeur.append(temp[1])
    colonestr = str("("+colone[0]+","+colone[1]+","+colone[2]+","+colone[3]+","+colone[4]+")")
    valeurstr = str("('"+valeur[0]+"','"+valeur[1]+"','"+valeur[2]+"','"+valeur[3]+"',"+valeur[4]+")")
    # Prepare dynamic SQL statement
    sql = "INSERT INTO Maison2 "+colonestr+" VALUES "+valeurstr+";"
    print(sql)

    if db_connection is not None:
        # Save Data into DB Table
        try:
            cursor.execute(sql)
            db_connection.commit()
        except MySQLdb.Error as error:
            print("Error executing SQL statement: {}".format(error))
            cache_message(msg)  # Cache the message if there is a database error
            reconnect_to_database()  # Reconnect to the database if there is an error
    else:
        cache_message(msg)  # Cache the message if there is no database connection

def cache_message(msg):
    message_cache.append(msg)

def process_message_cache():
    while message_cache:
        msg = message_cache.pop(0)
        on_message(None, None, msg)

def reconnect_to_database():
    global db_connection, cursor
    if db_connection is not None:
        db_connection.close()
    connect_to_database()

def on_subscribe(client, userdata, mid, granted_qos):
    pass

mqttc = mqtt_client.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect to MQTT Broker
mqttc.connect(MQTT_Broker, MQTT_Port, Keep_Alive_Interval)

# Connect to the database
connect_to_database()

# Continue the network loop
mqttc.loop_start()

try:
    while True:
        pass  # Keep the program running
except KeyboardInterrupt:
    mqttc.loop_stop()
    reconnect_to_database()
