from pwn import xor

KEY = bytes.fromhex('6670616a662628292a2526292a2968753125706f6a70666c61677b72346e64306d5f737472696e677d5925303838616e626c3b2e6a703a7034793035316b6a4a74696f7061646b5e242829626b3b6461')

for i in range(256):
    final = ""
    for e in KEY:
        final = final + chr(i ^ e)
    print(final)