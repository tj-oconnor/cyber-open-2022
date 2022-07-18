CFLAGS := -Wall -Wextra

# The name of this challenge, which is the name of the directory
# The generated .c file and executable will have this name
CHAL := $(notdir ${CURDIR})

all: $(CHAL)

clean:
	$(RM) $(CHAL).c $(CHAL)

# Generate the .c file with gen.py,
# passing the flag and the output filename to the script
$(CHAL).c: gen.py flag.txt
	./gen.py "$$(cat flag.txt)" $@

# Build the binary using the default rule for .c files
$(CHAL): $(CHAL).c

.PHONY: all clean
