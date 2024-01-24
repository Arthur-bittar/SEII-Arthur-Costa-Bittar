SRC = ./src
INC = ./inc
OBJ = ./obj
BIN = ./bin
APP = ./app

all: libraries applications
	
libraries: exemplo2.o

applications:
	gcc $(APP)/app.c $(OBJ)/*.o -I $(INC)/ -o $(BIN)/app

%.o: $(SRC)/%.c $(INC)/%.h
	gcc -c $< -I $(INC) -o $(OBJ)/$@
	
run: 
	$(BIN)/app

clean:
	rm -rf $(OBJ)/* $(BIN)/*