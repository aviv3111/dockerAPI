#!/usr/bin/python
from flask import Flask
import requests
from flask import request
import base64

def set_basic_auth(username, password):
        """this function return a basic-auth header for given username and password"""
        auth = (base64.b64encode((username+":"+password).encode("utf-8"))).decode("utf-8")
        return "Basic {parameters}".format(parameters=auth)


app = Flask(__name__)

@app.route("/")
@app.route("/check" , methods=['GET'])
def check():
     return "app work!"

@app.route("/backup", methods=['GET'])
def backup():
    username = request.args.get('username')
    password = request.args.get('password')
    IP = request.args.get('ip')
    basic_auth = set_basic_auth(username, password)
    header = {"Content-Type":"application/yang-data+json", "Authorization":basic_auth}
    uri = "https://{ip_add}/restconf/data/Cisco-IOS-XE-native:native?content=config".format(ip_add = IP)
    content = requests.get(url = uri, headers=header, verify=False)
    return content.text
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')