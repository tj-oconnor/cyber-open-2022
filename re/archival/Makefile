CFLAGS := -Wall -Wextra
ADIR := arc

all: extract arc.bin
clean:
	$(RM) extract arc.bin flag.png

runtest: all
	$(RM) -r tst
	mkdir tst
	./extract arc.bin tst
	diff -r arc tst
	$(RM) -r tst
	@echo Test passed!

extract: extract.c

arc.bin: archive.py flag.png flag.txt $(shell find $(ADIR))
	./archive.py "$$(cat flag.txt)" flag.png arc $@

flag.png: flag.txt
	convert -background white -pointsize 25 -fill black -gravity NorthWest caption:"$$(cat $<)" -flatten $@

.PHONY: all clean runtest
