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

char categories[8][15] = {
   "pwn\0",
   "re\0",
   "crypto\0",
   "forensics\0",
   "web\0"
};


void win() {
   system("/bin/cat flag.txt");
}

void print_cats() {
    for (int i=0; i<5; i++) {
        printf("- %i : %s\n",i,categories[i]);
    }
}

void vuln() {
    char buf[1];
    printf(" Would you like edit a category (Y/*) >>> ");
    scanf("%1s",buf);
    if (strcmp(buf,"Y")==0) {
       int num;
       printf(" Which category num >>> ");
       scanf("%d",&num);
       char val[20];
       printf(" Enter the new value >>> ");
       scanf("%20s",val);
       if (strcmp(val,"recon")==0) {

          printf("<<< Sorry, category not accepted.\n");
          system("echo Goodbye");
          sleep(1);
          exit(-1);
       }
       else {
          strcpy(categories[num],val);
          printf("<<< Categories updated.\n");
          print_cats();
       }
    }
}

int main() {
    printf("----------------------------------------------------------------------------\n");
    printf(" CTF Category Editor                                                        \n");
    printf("----------------------------------------------------------------------------\n");
    print_cats();
    printf("----------------------------------------------------------------------------\n");

    while (1==1) {
      vuln(); 
    }
}
