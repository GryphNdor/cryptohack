from pwn import * # pip install pwntools
from Crypto.Util.number import long_to_bytes
import codecs
import base64
import json

r = remote('socket.cryptohack.org', 13377, level = 'debug')

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


for i in range(0,101):
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    def yeetType(encType):
        if(encType == "utf-8"):
            string = ""
            for i in received["encoded"]:
                string += chr(i)
            return string
        if(encType == "bigint"):
            return bytes.fromhex(received["encoded"][2:]).decode("ASCII")
        if(encType == "hex"):
            bytes_object = bytes.fromhex(received["encoded"])
            return bytes_object.decode("ASCII")
        if(encType == "rot13"):
            return codecs.decode(received["encoded"],'rot13')
        if(encType == "base64"):
            b64bytes = (received["encoded"]).encode('ascii')
            b64 = base64.b64decode(b64bytes)
            return b64.decode('ascii')

    to_send = {
        "decoded" : yeetType(received["type"])
    }

    json_send(to_send)
