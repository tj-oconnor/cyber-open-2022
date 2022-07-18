#include <stdio.h>
#include <string.h>

void getflag(char *buff) {
    char key[] = {159, 63, 152, 164, 7, 53, 112, 119, 73, 27, 39, 70, 94, 32, 78, 189, 127, 146, 199, 252, 139, 134, 12, 198, 21, 201, 69};
    char st[] = {46, 210, 183, 168, 35, 201, 12, 159, 104, 207, 126, 103, 37, 105, 110, 226, 66, 67, 100, 170, 237, 58, 236, 244, 170, 153, 185};

    for (int i = 0; i < 13; i++) {
        if (i+1 < 27) {
            int tmp = st[i];
            st[i] = st[i+1];
            st[i+1] = tmp;
        }
    }

    for (int i = 0; i < 26; i++) {
        st[i+1] ^= st[i];
    }

    for (int i = 0; i < 27; i++) {
        key[i] = (char) ((((int)key[i]) + 23) & 0xFF);
    }

    for (int i = 0; i < 27; i++) {
        buff[i] = st[i] ^ key[i];
    }

    buff[27] = 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Wrong!!\n");
        return 1;
    }

    char flag[28];
    getflag(flag);

    if (strcmp(argv[1], flag)) {
        printf("Wrong!!\n");
    } else {
        printf("Correct!!\n");
    }
}
