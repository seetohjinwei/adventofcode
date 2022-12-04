CPPFLAGS=--std=c++20 -Wall
CC=c++ $(CPPFLAGS)

# to add another dependency, need to add the recipe here and in "copy.sh" $dependencies

parser.o: parser.h parser.cpp
	$(CC) -c parser.cpp -o bin/parser.o

clean:
	rm bin/* || true

reset: clean
	cp makefile_template makefile
	rm day*.cpp || true

d01: d01-build
	bin/day01
d01-build: day01.o  parser.o
	cd bin; \
	$(CC) -o day01 day01.o  parser.o
day01.o: day01.cpp
	$(CC) -c -o bin/day01.o day01.cpp

d02: d02-build
	bin/day02
d02-build: day02.o  parser.o
	cd bin; \
	$(CC) -o day02 day02.o  parser.o
day02.o: day02.cpp
	$(CC) -c -o bin/day02.o day02.cpp

d03: d03-build
	bin/day03
d03-build: day03.o  parser.o
	cd bin; \
	$(CC) -o day03 day03.o  parser.o
day03.o: day03.cpp
	$(CC) -c -o bin/day03.o day03.cpp

d04: d04-build
	bin/day04
d04-build: day04.o  parser.o
	cd bin; \
	$(CC) -o day04 day04.o  parser.o
day04.o: day04.cpp
	$(CC) -c -o bin/day04.o day04.cpp
