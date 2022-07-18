int printf(const char *format, ...);

int strcmp(const char *s1, const char *s2) {
    char key[] = {68, 51, 7, 13, 109, 8, 22, 119, 65, 3, 99, 25, 54, 23, 88, 29, 28, 53, 3, 101, 30, 35, 12, 107, 11, 81, 0, 5, 7, 23, 101, 92, 32};
    for (unsigned i = 0; i < sizeof(key); i++) {
        if (!s1[i] || !s2[i]) return 1;
        if ((s1[i] ^ key[i]) != s2[i]) return 1;
    }
    return 0;
}

int main(int argc, char **argv) {
    if (argc < 2) {
        printf("Wrong!!\n");
        return 1;
    }

    if (strcmp(argv[1], "0ar89WxG5KRwQHlsXjmUAlbXTc4d0rToF")) {
        printf("Wrong!!\n");
    } else {
        printf("Correct!!\n");
    }
}
