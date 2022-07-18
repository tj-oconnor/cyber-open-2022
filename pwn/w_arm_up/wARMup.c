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

void print_logo() {
 printf("--------------------------------------------\n");
 printf("                 (       *                  \n"); 
 printf("          (      )\\ )  (  `                 \n");
 printf(" (  (     )\\    (()/(  )\\))(     (          \n");
 printf(" )\\))( ((((_)(   /(_))((_)()\\   ))\\  `  )   \n");
 printf("((_)()\\ )\\ _ )\\ (_))  (_()((_) /((_) /(/(   \n");
 printf("_(()((_)(_)_\\(_)| _ \\ |  \\/  |(_))( ((_)_\\  \n"); 
 printf("\\ V  V / / _ \\  |   / | |\\/| || || || '_ \\) \n");
 printf(" \\_/\\_/ /_/ \\_\\ |_|_\\ |_|  |_| \\_,_|| .__/  \n");
 printf("                                    |_|     \n"); 
 printf("----------------------------------------------\n");
}

void gadget() {
  asm("pop {r0, r1, r2, pc}");
}

void sys_date() {
    system("date");
}

void vuln() {
    char buffer[8];
    printf("Would you know the time >>> ");
    gets(buffer);
    if (strncmp(buffer,"Y",1)==0) {
       sys_date();
    }
    else {
       exit(0);
    }
}

int main() {
    print_logo();
    vuln();
}
