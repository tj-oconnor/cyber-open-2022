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

int problem = 0;

void win() {
    FILE *fp;
    char buff[255];
    fp = fopen("flag.txt", "r");

    if (fp==NULL) {
        printf("<<< Error: flag.txt is not present");
        exit(0);
    }
    else {
        fscanf(fp, "%s", buff);
        printf("<<< Congratulations: %s\\n", buff );
    }

}

void print_logo() {
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXOkkOOOOOOOOOO000KXXNWMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx'...............'',;:loxOKNWMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.........................';lkKWMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.............................'lONMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx................................cOWMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx.................................'dXMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx...................................oNMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........':::::;;,,'................,OMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........oNWWWWWNNXK0Od:............'kMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMNd'..........;0MMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMMXc..........oNMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMMXc.........:KMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMMK:........;0WMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMMO,.......;0WMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMWx.......c0WMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMXl.....'dXWMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMM0;....c0WMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMWx..'cONMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWx........dWMMMMMMMMMMMMKkkKWMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMWNXK0000KXNWMMWx........dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMWN0dl;,'.....';:ldkl........dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMW0o;..........................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMW0l'............................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMNx,..............................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMNo................................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMWx.................................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMK;.................................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMk'.................................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMWk'.................................dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMO,................................'kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMNl................................:KMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMM0;..............................,kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMW0:...........................,lkWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMKo'........................c0NWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMNOl'...................'cONMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMWKxc,.............,cd0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMWX0xdllccclldxOXWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMWWWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
    printf("MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM\n");
}

void vuln() {
    char buf[256];
    problem += 1;
    if (problem==98) {
       problem=100;
    }
    else if (problem==99) {
       printf("<<< Time to Take a Break and Get Some Fresh Air");
       sleep(5);
       exit(0);
    }

    else {
       printf("Enter a word and Ill email you a list of words that ryhme >>> ");
       scanf("%256s",buf);
       printf("<<< Email functonality not implemented. Try back later with your word : ");
       printf(buf);
       printf("\n");
    }
}

int main() {
    print_logo();
    printf("----------------------------------------------------------------------------\n");
    printf(" A poet's mission is to make words do more work than they normally do       \n");
    printf(" to make them work on more than one level.                  - Jay Z         \n");
    printf("----------------------------------------------------------------------------\n");
 
    while (1==1) {
      vuln(); 
    }
}
