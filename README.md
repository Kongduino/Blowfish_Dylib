# Blowfish_Dylib

A Blowfish cipher dynamic library for use with Python, Xojo, etc... like my [Chacha20_Dylib](https://github.com/Kongduino/Chacha20_Dylib). It is based on [Paul Kocher's implementation](https://www.schneier.com/academic/blowfish/download/).

Yes, it's an old cipher, but it's easy to use, and I am trying to make more small dylibs, so this was an easy one to make.

```sh
% make
gcc -Ofast -g   -c -o blowfish.o blowfish.c
gcc -Ofast -g   -c -o blowfish_test.o blowfish_test.c
gcc -Ofast -g *.c
gcc -dynamiclib blowfish.o -o blowfish.dylib
gcc *.o -o blowfish_test
rm *.o
./blowfish_test
DF333FD2 30A71BB4
Test encryption OK.
Test decryption OK.
cd Python ; ./Test.py; ./Test_Long.py
Init
b'ABCD' b'EFGH'
Encrypt
b'\x95\xf6\x0ba' b'A\x98\xb9\x15'
Decrypt
b'ABCD' b'EFGH'
Init
   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|54 68 69 73 20 69 73 20 61 20 6c 6f 6e 67 20 73 | |This is a long s|
01.|74 72 69 6e 67 2c 20 6e 6f 74 20 70 61 64 64 65 | |tring, not padde|
02.|64 2e 2e 2e 00 00 00 00                         | |d...............|
   +------------------------------------------------+ +----------------+
Encrypt
   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|6c 2b e4 12 b3 c2 fb 2a f1 ce 47 7d 5e ac 06 b0 | |l+.....*..G}^...|
01.|05 2b fe e7 4e 9a 84 27 5d e9 4a fb 2a 14 85 5e | |.+..N..'].J.*..^|
02.|20 bc ed 01 eb cf d9 bc                         | | ...............|
   +------------------------------------------------+ +----------------+
Decrypt
   +------------------------------------------------+ +----------------+
   |.0 .1 .2 .3 .4 .5 .6 .7 .8 .9 .a .b .c .d .e .f | |      ASCII     |
   +------------------------------------------------+ +----------------+
00.|54 68 69 73 20 69 73 20 61 20 6c 6f 6e 67 20 73 | |This is a long s|
01.|74 72 69 6e 67 2c 20 6e 6f 74 20 70 61 64 64 65 | |tring, not padde|
02.|64 2e 2e 2e 00 00 00 00                         | |d...............|
   +------------------------------------------------+ +----------------+
```