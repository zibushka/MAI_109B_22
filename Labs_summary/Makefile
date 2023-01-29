CPPFILES = $(wildcard *.cpp)
OBJFILES = $(CPPFILES:.cpp=.o)
OUT      = main


CC      = g++
CFLAGS = -std=c++17 -Wall -O0 -fsanitize=address
LDLIBS = -lstdc++ -lm

$(OUT): $(OBJFILES)

.PHONY: clean
clean:
	rm -f $(OBJFILES) $(OUT)


