# build an executable named myprog from myprog.c

all: memallocator.c 
	gcc -g -Wall -o memallocator memallocator.c

run: all
	./memallocator $(tot_ram) $(mem_procent) $(time)
	make clean

clean: 
	$(RM) memallocator