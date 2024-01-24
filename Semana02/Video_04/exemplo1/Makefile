all:
	gcc -c ./src/exemplo2.c -I ./inc -o ./obj/exemplo2.o
	gcc ./app/app.c ./obj/*.o -I ./inc/ -o ./bin/app

run: 
	./bin/app


clean:
	rm ./obj/* ./bin/*