import random
import base64
from subprocess import run, PIPE

from urllib.request import urlopen as getapi
from urllib.parse import quote_plus as urlencode
from json import loads as jsonify
from requests import get as decodeurl

class Config:
    id = 696973408000409626 # BOT ID
    prefix = 'Todo.' # your prefix here
    class owner:
        load = "<a:dcloadv10:698837945423233075>"
        id = 552492140270452736 # YOUR USER ID
        name = 'Dispenser Gans'
prefix = 'Todo.'

def urlify(word):
    return urlencode(word).replace('+', '%20')

def jsonisp(url):
    return decodeurl(url).json()

def api(url):
    return jsonify(getapi(url).read())
    
def insp(url):
    return decodeurl(url).text
    
def getPrefix():
    return prefix

def bin(text):
    result = " ".join(f"{ord(i):08b}" for i in text) # THANKS STACK OVERFLOW! UWU
    return result.replace(' ', '')

def encodeb64(text):
    message_bytes = text.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    return base64_message