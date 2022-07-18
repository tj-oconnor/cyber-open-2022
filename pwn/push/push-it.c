#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <sys/syscall.h>
#include <time.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char shell[] = {'/','b','i','n','/','s','h','\0'};
int r = 0;

void push_1() {
    asm("push 0x58585858; ret");
}

void push_2() {
    asm("push 0x0f050f05; ret");
}

void push_3() {
    asm("push 0x58580f05; ret");
}

void push_4() {
    asm("push 0x0f055858; ret");
}


char * push_text[] = {
  "push 0x58585858; ret",
  "push 0x0f050f05; ret",
  "push 0x58580f05; ret",
  "push 0x0f055858; ret"
};

void * push_addr[] = {
  &push_1+4,
  &push_2+4,
  &push_3+4,
  &push_4+4,
};


void vuln() {
    char buffer[8];
    printf("~ Would you like another push (Y/*) >>> ");
    gets(buffer);
    if (strcmp(buffer,"Y")==0) {
       printf("~ %s | %p\n",push_text[r],push_addr[r]);
       r = r +1;
    }
}

int main() {
    printf("----------------------------------------------------------------------------\n");
    printf(" ~ You stay the course, you hold the line you keep it all together        ~ \n");
    printf(" ~ You're the one true thing I know I can believe in                      ~ \n");
    printf(" ~ You're all the things that I desire you save me, you complete me       ~ \n");
    printf(" ~                                              - Push, Sarah McLachlan.  ~ \n");
    printf("----------------------------------------------------------------------------\n");
    printf("<<< Push your way to /bin/sh at : %p\n", shell);
    printf("----------------------------------------------------------------------------\n");

    while (1) {
      vuln();
    }
}
