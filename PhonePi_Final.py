from flask import Flask
from flask_sockets import Sockets
import socket
import json
import matplotlib.pyplot as plt
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

hostname = socket.gethostname()
IPAddr = get_ip()
print("Your Computer Name is: " + hostname)
print("Your Computer IP Address is: " + IPAddr)
print("Enter {0}:5000 in the app [PhonePi] and select the sensors to stream. For PhonePi+ just enter {0}, without the port\n\n".format(IPAddr))

app = Flask(__name__)
sockets = Sockets(app)


@sockets.route('/accelerometer')
def echo_socket(ws):
    f = open("accelerometer.txt", "a")
    cnt =0
    while cnt<1:
        message = ws.receive()
        acc = json.loads(message)
        X = acc.get("dataX")
        Y = acc.get("dataY")
        Z = acc.get("dataZ")
        print("Accelerometer Data: \nX=" + str(X) + " Y=" + str(Y)+" Z="+str(Z)+"\n")
        #ws.send(message)
        #print(message, file=f)
        cnt = cnt+1
    f.close()


@sockets.route('/gyroscope')
def echo_socket(ws):
    f = open("gyroscope.txt", "a")
    cnt = 0
    while cnt <1:
        message = ws.receive()
        gyro = json.loads(message)
        X1 = gyro.get("dataX")
        Y1 = gyro.get("dataY")
        Z1 = gyro.get("dataZ")
        print("Gyroscope Data: \n X=" + str(X1) + " Y=" + str(Y1)+" Z="+str(Z1)+"\n")
        #ws.send(message)
        #print(message, file=f)
        cnt = cnt+1
    f.close()


@sockets.route('/magnetometer')
def echo_socket(ws):
    f = open("magnetometer.txt", "a")
    cnt =0
    while cnt<1:
        message = ws.receive()
        mag = json.loads(message)
        X2 = mag.get("dataX")
        Y2 = mag.get("dataY")
        Z2 = mag.get("dataZ")
        print("Magnetometer Data: \nX=" + str(X2) + " Y=" + str(Y2)+" Z="+str(Z2)+"\n")
        #ws.send(message)
        #print(message, file=f)
        cnt =cnt+1
    f.close()


@sockets.route('/orientation')
def echo_socket(ws):
    f = open("orientation.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/stepcounter')
def echo_socket(ws):
    f = open("stepcounter.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/thermometer')
def echo_socket(ws):
    f = open("thermometer.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/lightsensor')
def echo_socket(ws):
    f = open("lightsensor.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/proximity')
def echo_socket(ws):
    f = open("proximity.txt", "a")
    while True:
        message = ws.receive()
        print(message)
        ws.send(message)
        print(message, file=f)
    f.close()


@sockets.route('/geolocation')
def echo_socket(ws):
    f = open("geolocation.txt", "a")
    cnt = 0
    while cnt<1:
        message = ws.receive()
        loc = json.loads(message)
        loc_data = loc.get("data")
        loc_data1 = loc_data["coords"]
        #loc_data1 = json.loads(loc_data)

        #loc_coords = loc_data("coords")
        #loc_coords1 = json.loads(loc_coords)
        longitude = loc_data1.get("longitude")
        latitude = loc_data1.get("latitude")
        altitude = loc_data1.get("altitude")
        #print(type(message))
       ## print(type(loc_data1))
       ## print(loc_data1.items())
        print("GPS Data: \n Latitude=" + str(longitude) + " Longitude=" + str(latitude)+" Altitude="+str(altitude)+"\n")
       # return longitude,latitude
        #ws.send(message)
       # print(message, file=f)
        cnt = cnt+1
    f.close()


@app.route('/')
def hello():
    return 'Hello World!'


if __name__ == "__main__":
    from gevent import pywsgi
    from geventwebsocket.handler import WebSocketHandler
    server = pywsgi.WSGIServer(
        ('0.0.0.0', 5000), app, handler_class=WebSocketHandler)
    server.serve_forever()
