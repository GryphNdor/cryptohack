from pwn import *

conn = remote('challenges.ctfd.io',30468)
conn.recvline()
conn.send('flag{')
conn.recvuntil(b' ', drop=True)
conn.recvline()
conn.send('flag{')
print(conn.recvline())
conn.close()