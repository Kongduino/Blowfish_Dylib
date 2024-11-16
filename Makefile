.POSIX:
TARGET = blowfish
CC = gcc
CFLAGS = -Ofast -g

# The list of object files.
OBJS =  blowfish.o	blowfish_test.o

# the list of files to clean
TOCLEAN = blowfish.dylib $(OBJS)

RM ?= rm -f

all: $(TARGET)
clean:
	$(RM) $(TOCLEAN)

blowfish: $(OBJS)
	$(CC) $(CFLAGS) *.c
	$(CC) -dynamiclib blowfish.o -o $(TARGET).dylib
	$(CC) *.o -o blowfish_test
	rm *.o *.out
	./blowfish_test
	cd Python ; ./Test.py; ./Test_Long.py

install:
	cp $(TARGET).dylib /usr/local/lib/