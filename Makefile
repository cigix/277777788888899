CC=gcc
CFLAGS=-Os -g3

PROJECT=persistence
SRC=persistence

##########

OBJ=$(addsuffix .o, $(SRC))
PROJECTOBJ=$(PROJECT).o

all: $(PROJECT)

$(PROJECTOBJ): $(OBJ)

clean:
	$(RM) $(PROJECT) $(PROJECTOBJ) $(OBJ)

open: $(PROJECTOBJ)
	objdump -S $(PROJECTOBJ) | less
