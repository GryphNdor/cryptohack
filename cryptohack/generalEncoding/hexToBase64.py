import codecs

def thing(h):
    b64 = codecs.encode(codecs.decode(h, 'hex'), 'base64').decode()

    print(b64)

thing('YXZvY2Fkb3NfU292aWV0X2Jvb3plcw==')