import requests

def get():
    ip = requests.get("https://api.ipify.org")
    return ip.text