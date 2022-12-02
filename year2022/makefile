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
