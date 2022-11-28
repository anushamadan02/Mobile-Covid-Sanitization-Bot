# covid_bot

# Mosquitto Installation
```
1)sudo apt-add-repository ppa:mosquitto-dev/mosquitto-ppa
2)sudo apt-get install mosquitto
3)sudo apt-get install mosquitto-clients
4)wget https://mosquitto.org/files/source/mosquitto-2.0.10.tar.gz
5)tar -zxvf  mosquitto-2.0.10.tar.gz 
6)pip install paho-mqtt
```
# Flask Installation

```
pip install -U Flask
```

# Steps to run
```
1)Run stream.py
2)Run mosquitto_sub -h test.mosquitto.org -t paho/temperature
```

