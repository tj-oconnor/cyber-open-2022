#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h>

int main(void) {
    // Disable buffering
    setvbuf(stdin, 0, 2, 0);
    setvbuf(stdout, 0, 2, 0);

    // Buffer to overflow, cleared out
    char buf[1024];
    memset(buf, 0, sizeof(buf));

    // "Story"
    puts("GIBSON S390X");
    puts("Enter payroll data:");
    read(0, buf, 2000);
    
    // Doesn't actually affect much, since the data we leak is after this.
    // Will have to encode gadget / format string info though
    puts("Processing data...");
    // Make this a long for convenience - otherwise stack data dets on a weird 4-byte boundary
    for (unsigned long int i = 0; i < sizeof(buf); i++) {
        buf[i] ^= 0x52;
    }

    // Simulate work
    sleep(0.5);
    
    // Info Leak
    printf(buf);

    // Only executes once before return, but binary is non-PIE and no canaries so we can send it back around to main()
}
