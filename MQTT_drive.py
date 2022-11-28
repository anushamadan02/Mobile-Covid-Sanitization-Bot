
import paho.mqtt.client as mqtt

def Drive_MQTT(steering):

    mqttc = mqtt.Client()

    mqttc.connect("test.mosquitto.org")
    mqttc.loop_start()

   
    mqttc.publish("paho/temperature", steering)