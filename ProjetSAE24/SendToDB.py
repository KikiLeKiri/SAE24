from paho.mqtt import client as mqtt_client
import MySQLdb

db_connection = MySQLdb.connect(host='localhost',user='root',passwd='toto',db='mqttdb')
cursor = db_connection.cursor()

# MQTT Settings
MQTT_Broker = 'broker.hivemq.com'
MQTT_Port = 1883
Keep_Alive_Interval = 60
MQTT_Topic = "IUT/GR11/Colmar2023/SAE2.04/Maison1"

# Subscribe
def on_connect(client, userdata, flags, rc):
  mqttc.subscribe(MQTT_Topic, 0)

def on_message(mosq, obj, msg):
  colone = []
  valeur = []
  print("received message =", str(msg.payload.decode("utf-8")))
  message_recu = str(msg.payload.decode("utf-8"))
  message = message_recu.split(',')
  for e in message:
    temp = e.split('=')
    colone.append(temp[0])
    valeur.append(temp[1])
  colonestr = str("("+colone[0]+","+colone[1]+","+colone[2]+","+colone[3]+","+colone[4]+")")
  valeurstr = str("('"+valeur[0]+"','"+valeur[1]+"','"+valeur[2]+"','"+valeur[3]+"',"+valeur[4]+")")
  # Prepare dynamic sql-statement
  sql = "INSERT INTO Maison1 "+colonestr+" VALUES "+valeurstr+";"
  print(sql)

  # Save Data into DB Table
  try:
      cursor.execute(sql)
  except MySQLdb.Error as error:
      print("Error: {}".format(error))
  db_connection.commit()

def on_subscribe(mosq, obj, mid, granted_qos):
  pass

mqttc = mqtt_client.Client()

# Assign event callbacks
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe

# Connect
mqttc.connect(MQTT_Broker, int(MQTT_Port), int(Keep_Alive_Interval))

# Continue the network loop & close db-connection
mqttc.loop_forever()
db_connection.close()