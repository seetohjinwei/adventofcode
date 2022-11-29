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
