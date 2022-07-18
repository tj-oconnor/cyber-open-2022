CFLAGS := -Wall -Wextra

# The name of this challenge, which is the name of the directory
# The generated .c file and executable will have this name
CHAL := $(notdir ${CURDIR})

all: $(CHAL) test

clean:
	$(RM) $(CHAL).c $(CHAL) test

# Generate the .c file with gen.py,
# passing the flag and the output filename to the script
$(CHAL).c: gen.py flag.txt
	./gen.py "$$(cat flag.txt)" $@ util.h

# Challenge binary
$(CHAL): $(CHAL).c util.h

# Test binary
test: test.c util.h

# Rule for building binaries
# Same as default, but only uses the first dependency
$(CHAL) test:
	$(LINK.c) $< $(LOADLIBES) $(LDLIBS) -o $@

PHONY: all clean
