SRC = ./src
INC = ./inc
OBJ = ./obj
BIN = ./bin
APP = ./app

all: libraries applications
	

libraries:
	gcc -c $(SRC)/exemplo2.c -I $(INC) -o $(OBJ)/exemplo2.o

applications:
	gcc $(APP)/app.c $(OBJ)/*.o -I $(INC)/ -o $(BIN)/app

run: 
	$(BIN)/app

clean:
	rm $(OBJ)/* $(BIN)/*