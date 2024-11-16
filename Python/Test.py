#!/usr/bin/python3
from ctypes import *
import platform, os, sys, random
from hexdump import hexDump

pl = platform.system()
if pl == 'Darwin':
  bfs = CDLL('../blowfish.dylib')
elif pl == 'Linux':
  bfs = CDLL('../blowfish.so')

# typedef struct {
#   unsigned int P[16 + 2];
#   unsigned int S[4][256];
# } BLOWFISH_CTX;

BLOWFISH_CTX = bytes(((16 + 2) * 4) + (4 * 4 * 256))
BLOWFISH_CTXB = cast(BLOWFISH_CTX, POINTER(c_char))
key = b"TESTKEY"
KEY_SIZE = len(key)
keyB = cast(key, POINTER(c_char))

L = b'ABCD'
R = b'EFGH'
LB = cast(L, POINTER(c_char))
RB = cast(R, POINTER(c_char))

print("Init")
bfs.Blowfish_Init(BLOWFISH_CTXB, keyB, KEY_SIZE);
print(f"{L} {R}")
print("Encrypt")
bfs.Blowfish_Encrypt(BLOWFISH_CTXB, LB, RB)
print(f"{L} {R}")
print("Decrypt")
bfs.Blowfish_Decrypt(BLOWFISH_CTXB, LB, RB)
print(f"{L} {R}")

