#include <stdlib.h>
#include <stdio.h>
#include <string.h>
#include <sys/types.h>
#include <sys/wait.h>
#include <unistd.h>

#define BSZ 39

int main(int argc, char **argv) {
    if (argc < 2 || strlen(argv[1]) != 39) {
        printf("Wrong!!\n");
        return 1;
    }

    int p1[2], p2[2], p3[2], p4[2];
    pipe(p1);
    pipe(p2);
    pipe(p3);
    pipe(p4);

    pid_t pid1 = fork();
    if (pid1 == 0) {
        close(p1[1]); close(p2[0]); close(p2[1]); close(p3[0]); close(p3[1]); close(p4[0]);
        char buff[BSZ], prev = 0;
        ssize_t ret;
        while ((ret = read(p1[0], buff, BSZ)) > 0) {
            for (ssize_t i = 0; i < ret; i++) {
                buff[i] ^= prev;
                prev = buff[i];
            }
            write(p4[1], buff, ret);
        }
        close(p4[1]);
        exit(0);
    }

    pid_t pid2 = fork();
    if (pid2 == 0) {
        close(p1[0]); close(p1[1]); close(p2[0]); close(p2[1]); close(p3[1]); close(p4[0]); close(p4[1]);
        char buff[39];
        char exv[] = {153, 105, 59, 252, 157, 26, 160, 25, 211, 169, 135, 221, 130, 202, 97, 56, 255, 85, 94, 206, 175, 156, 166, 13, 211, 100, 154, 234, 39, 134, 111, 127, 1, 224, 173, 72, 221, 97, 154};
        ssize_t ret;
        ssize_t rem = sizeof(buff);
        char *ptr = buff;
        while ((ret = read(p3[0], ptr, rem)) > 0) {
            rem -= ret;
            ptr += ret;
        }

        if (memcmp(buff, exv, sizeof(buff))) {
            printf("Wrong!!\n");
        } else {
            printf("Correct!!\n");
        }
        exit(0);
    }

    pid_t pid3 = fork();
    if (pid3 == 0) {
        close(p1[0]); close(p2[1]); close(p3[0]); close(p3[1]); close(p4[0]); close(p4[1]);
        char buff[BSZ];
        ssize_t ret;
        while ((ret = read(p2[0], buff, BSZ)) > 0) {
            for (ssize_t i = 0; i < ret; i++) {
                buff[i] ^= 0x56;
            }
            write(p1[1], buff, ret);
        }
        close(p1[1]);
        exit(0);
    }

    pid_t pid4 = fork();
    if (pid4 == 0) {
        close(p1[0]); close(p1[1]); close(p2[0]); close(p3[0]); close(p3[1]); close(p4[0]); close(p4[1]);
        write(p2[1], argv[1], strlen(argv[1]));
        close(p2[1]);
        exit(0);
    }

    pid_t pid5 = fork();
    if (pid5 == 0) {
        close(p1[0]); close(p1[1]); close(p2[0]); close(p2[1]); close(p3[0]); close(p4[1]);
        char buff[BSZ];
        char key[] = {187, 85, 98, 172, 252, 95, 128, 91, 179, 192, 234, 215, 168, 133, 10, 90, 248, 102, 89, 170, 194, 147, 145, 40, 255, 120, 156, 138, 102, 164, 68, 58, 115, 247, 143, 8, 250, 117, 186};
        int j = 0;
        ssize_t ret;
        while ((ret = read(p4[0], buff, BSZ)) > 0) {
            for (ssize_t i = 0; i < ret; i++) {
                buff[i] ^= key[j++];
                if (j == sizeof(key)) j = 0;
            }
            write(p3[1], buff, ret);
        }
        close(p3[1]);
        exit(0);
    }

    close(p1[0]); close(p1[1]); close(p2[0]); close(p2[1]); close(p3[0]); close(p3[1]); close(p4[0]); close(p4[1]);

    int stat_loc;
    while (wait(&stat_loc) > 0);
}
