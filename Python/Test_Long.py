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

def PadString(myString):
    while len(myString) % 8 > 0:
        myString += b'\x00'
    return myString

def EncryptBlock(plaintext, ln):
  cipher = b''
  for i in range(0, ln, 8):
    L = plain[i:i+4]
    R = plain[i+4:i+8]
    LB = cast(L, POINTER(c_char))
    RB = cast(R, POINTER(c_char))
    bfs.Blowfish_Encrypt(BLOWFISH_CTXB, LB, RB)
    cipher += L + R
  return cipher

def DecryptBlock(cipher, ln):
  deciphered = b''
  for i in range(0, ln, 8):
    L = cipher[i:i+4]
    R = cipher[i+4:i+8]
    LB = cast(L, POINTER(c_char))
    RB = cast(R, POINTER(c_char))
    bfs.Blowfish_Decrypt(BLOWFISH_CTXB, LB, RB)
    deciphered += L + R
  return deciphered

BLOWFISH_CTX = bytes(((16 + 2) * 4) + (4 * 4 * 256))
BLOWFISH_CTXB = cast(BLOWFISH_CTX, POINTER(c_char))
key = b"TESTKEY"
KEY_SIZE = len(key)
keyB = cast(key, POINTER(c_char))

print("Init")
bfs.Blowfish_Init(BLOWFISH_CTXB, keyB, KEY_SIZE);
if len(sys.argv) == 2:
    plain = PadString(bytes(sys.argv[1], encoding='ascii'))
else:
    plain = PadString(b'This is a long string, not padded...')
ln = len(plain)
hexDump(plain)

print("Encrypt")
cipher = EncryptBlock(plain, ln)
hexDump(cipher)

print("Decrypt")
deciphered = DecryptBlock(cipher, len(cipher))
hexDump(deciphered)

