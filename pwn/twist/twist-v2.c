#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <stdbool.h>
#include <unistd.h>
#include <stdio.h>
#include <stdint.h>

void print_logo() {
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMMMMMMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWWWNK0O0XWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWMMWWNKkxol:cdkKWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXKOxl:;,',cxXWMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWN0xl:;,''',';xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWN0dc,'''''''',l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNOl,',''''''',':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKl;,'',',,',,''';oONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMWMMWO:','''',;:::;,'',',cONWMWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMWk;''''';oOKXXXKOo;','';xNWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMKc',''':ONWMMMMWMNk:'',',kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMWWW0:''','oNWMMWMWMMMXl','''cKWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMWWXl'''''cKWWWWWMWWW0:''''':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMWMWKl,',''ckXNWWWWXk:''''''lXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMWMXx;,''',:codol:,'''',,:OWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKx:,'''''''''''''',l0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWWKl'''',,'','',,:xXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWXd;',,',,'',',lkXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMMWWMMWXx:,,,',,''',cd0NWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMWMMWKd:,,,''';codkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMMWNOl;'',;codkKNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMXOdlloxk0XNWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM");
    printf("\nMMMMMMMMMMMMMMMMMMMMMMMNXXNWMMWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM/bin/sh");
    printf("\n--------------------------------------------------------------------------------------------");
    printf("\n     Welcome to Twist v2.0. Some file contents may have shifted on upload.                  ");
    printf("\n--------------------------------------------------------------------------------------------");
}


void pop_rbx() {
    asm("pop %rbx; ret;");
}

void ret_syscall() {
    asm("syscall; ret;");
}

void pop_rdi() {
    asm("pop %rdi; ret;");
}

void pop_rcx() {
    asm("pop %rcx; ret;");
}

void pop_rax() {
    asm("pop %rax; ret;");
}


void pop_rdx() {
    asm("pop %rdx; ret;");
}

void pop_rsi() {
    asm("pop %rsi; ret;");
}


void debug_mode() {
    uint64_t rax;
    __asm__ __volatile__ ("mov %%rax, %0" :"=rm"(rax) 
    );

    uint64_t rbx;
    __asm__ __volatile__ ("mov %%rbx, %0" :"=rm"(rbx) 
    );  

    uint64_t rcx;
    __asm__ __volatile__ ("mov %%rcx, %0" :"=rm"(rcx) 
    );  

    uint64_t rdx;
    __asm__ __volatile__ ("mov %%rdx, %0" :"=rm"(rdx) 
    );  

    uint64_t rsi;
    __asm__ __volatile__ ("mov %%rsi, %0" :"=rm"(rsi) 
    );  

    uint64_t rdi;
    __asm__ __volatile__ ("mov %%rdi, %0" :"=rm"(rdi) 
    );  

    printf("\n %8p | %8p | %8p | %8p | %8p | %8p",rax,rbx,rcx,rdx,rdi,rsi);

}

int main(int argc, char* argv[]) {

    print_logo();
    printf("\n     Debug Mode Enabled; calling %p",&debug_mode);
    printf("\n--------------------------------------------------------------------------------------------");
    debug_mode();
    printf("\n--------------------------------------------------------------------------------------------");
    printf("\n     You can dance in a hurricane but only if you are standing in the eye >>> ");
    char s[8];
    gets(s);

}
