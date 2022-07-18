#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>
#include <time.h>

__attribute__((constructor)) void ignore_me() {
    setbuf(stdin, NULL);
    setbuf(stdout, NULL);
    setbuf(stderr, NULL);
}

char shell[] = {'/','b','i','n','/','s','h','\0'};

void print_logo() {
  system("echo ~USCG~");
}

int problem(int a, int b, int t1, int r) {
 if (t1%10==0) {
    return (a-b+t1+r);
 }
 else if (t1%10==0) {
    return (a+b-t1+r);
 }
 else if (t1%10==1) {
    return (a+b+t1-r);
 }
 else if (t1%10==2) {
    return (a-b-t1+r);
 }
 else if (t1%10==3) {
    return (a-b+t1-r);
 }
 else if (t1%10==4) {
    return (a+b-t1-r);
 }
 else if (t1%10==5) {
    return (a*b+t1+r);
 }
 else if (t1%10==6) {
    return (a+b*t1+r);
 }
 else if (t1%10==7) {
    return (a+b+t1*r);
 }
 else if (t1%10==8) {
    return (a*b*t1+r);
 }
 else {
    return (a+b+t1+r);
 }


}

void check(int n1, int n2, int t1) {
  int r;
  printf("Nonce 1: %i\n",n1);
  printf("Nonce 2: %i\n",n2);
  printf("Your Response >>> ");
  scanf("%i", &r);
  if (problem(n1,n2,t1,r)!=1337) {
    printf("<<< Incorrect. Exiting\n");
    exit(0);
  }
  else {
    printf("<<< Correct. Continuing\n");
  }
}

void overflow() {
  char s[8];
  printf("Throw Your Exploit >>>");
  gets(s);
}

void vuln() {
  srand(time(NULL));   

  for (int i=1;i<100;i++) {
    int n1 = rand();
    int n2 = rand();
    check(n1,n2,i);
  }
  while (1==1) {
   overflow();
  }
}

int main(int argc, char* argv[]) {
  vuln();
}