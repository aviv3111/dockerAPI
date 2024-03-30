
import requests
import argparse
import base64
requests.packages.urllib3.disable_warnings()

def set_basic_auth(username, password):
        """this function return a basic-auth header for given username and password"""
        auth = (base64.b64encode((username+":"+password).encode("utf-8"))).decode("utf-8")
        return "Basic {parameters}".format(parameters=auth)



def main():
    parser =argparse.ArgumentParser()
    required_arg = parser.add_argument_group("Required named arguments")
    required_arg.add_argument(
        "--ip",
        help="IP of Traget host",
        required=True )
    required_arg.add_argument(
        "-u",
        "--username",
        help="Username",
        required=True
    )
    required_arg.add_argument(
        "-p",
        "--password",
        help="username password",
        required=True
    )
    
    arg = parser.parse_args()

    url = "https://{ip}/restconf/data/Cisco-IOS-XE-native:native?content=config".format(ip= arg.ip)
    auth = set_basic_auth(username=arg.username, password=arg.password)
    headers = {
    'Authorization': auth, 'Content-Type':"application/yang-data+json"}
    response = requests.get(url, headers=headers, verify=False)
    content = response.text
    print (content)
    
    
if __name__ == "__main__":
    main()