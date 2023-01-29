CXX       := g++
CXX_FLAGS := -std=c++17 -Wall -O0 -fsanitize=address

BIN     := bin
LAB     := lab23
SRC     := src
INCLUDE := include
LIB     := lib
TESTS   := tests
LIBRARIES   := -lstdc++ -lm
EXECUTABLE  := main


build: $(LAB)/$(BIN)/$(EXECUTABLE)

run: clean build
	clear
	@echo "Executing..."
	./$(LAB)/$(BIN)/$(EXECUTABLE)

$$(LAB)/(BIN)/$(EXECUTABLE): $(SRC)/*.cpp
	@echo "Building..."
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -L$(LIB) $^ -o $@ $(LIBRARIES)

$(LAB)/$(TESTS)/$(EXECUTABLE): $(SRC)/*.cpp
	@echo "Building..."
	$(CXX) $(CXX_FLAGS) -I$(INCLUDE) -L$(LIB) $^ -o $@ $(LIBRARIES)

clean:
	@echo "Clearing..."
	-rm $(LAB)/$(BIN)/*

test: clean
	clear
	@echo "Run tests..."
	./$(LAB)/$(TESTS)/$(EXECUTABLE)



